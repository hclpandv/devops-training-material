#!/usr/bin/env python

# -------------------------------------------------------------------------------------------------
# Version    : 1.0
# Date       : 24-FEB-2023
# Description: Custom Script and Plugin to populate/sync ansible inventory from Azure subscription   
# Maintainer : Vikas Pandey, <vikiscripts@gmail.com>
# features   :  - Creates 2 child groups for windows and linux
#               - Excludes PowerOff VMs
#               - Exclude Resource Groups and VM names based on supplied patters via Env Variables
#               - Tested and suitable with ansible tower
# -------------------------------------------------------------------------------------------------
import os
import json
import requests
import re

def get_azure_vms(resource_group_name=None):
    # Replace the following values with your Azure subscription information
    client_id = os.environ.get('AZURE_CLIENT_ID', None)
    client_secret = os.environ.get('AZURE_SECRET', None)
    tenant_id = os.environ.get('AZURE_TENANT', None)
    subscription_id = os.environ.get('AZURE_SUBSCRIPTION_ID', None)
    subscription_name = os.environ.get('AZURE_SUBSCRIPTION_NAME', None)
    exclude_host_filters = os.getenv("EXCLUDE_HOST_FILTERS", "").split(",")
    exclude_rg_filters = os.getenv("EXCLUDE_RG_FILTERS", "").split(",")

    # Request a token for authentication
    token_endpoint = "https://login.microsoftonline.com/{}/oauth2/token".format(tenant_id)
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "resource": "https://management.azure.com/"
    }
    response = requests.post(token_endpoint, headers=headers, data=data)
    if response.status_code != 200:
        raise Exception("Failed to get authentication token")
    token = response.json()["access_token"]

    vms = []
    vm_endpoint = "https://management.azure.com/subscriptions/{}/providers/Microsoft.Compute/virtualMachines?api-version=2022-11-01".format(subscription_id)
    while True:
        headers = {
            "Authorization": "Bearer {}".format(token),
            "Content-Type": "application/json"
        }
        response = requests.get(vm_endpoint, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to get list of VMs")
        result = response.json()
        if 'value' in result:
            vms.extend(result['value'])
        if 'nextLink' not in result:
            break
        vm_endpoint = result['nextLink']

    # Format the VMs as Ansible inventory
    inventory = {
        "IG_{}_windows".format(subscription_name): {
            "hosts": [],
            "vars": {}
        },
        "IG_{}_linux".format(subscription_name): {
            "hosts": [],
            "vars": {}
        },
        "_meta": {
            "hostvars": {}
        }
    }
    for vm in vms:
        name = vm["name"]
        location = vm["location"]
        resource_type = vm["type"]
        resource_group = vm["id"].split("/")[4]
        provisioning_state = vm["properties"]["provisioningState"]
        if "zones" in vm:
            availability_zone = vm["zones"]
        else:
            availability_zone = None
        os_type = vm["properties"]["storageProfile"]["osDisk"]["osType"].lower()
        # Exclusions
        #exclude_host_filters = [
        #    "^RTA",
        #    "^aks",
        #    "^FW",
        #    "AZEIMG",
        #    ".*WVD.*",
        #    "^dns",
        #    ".*RAS.*",
        #    ".*VPN.*",
        #    ".*CVAD.*",
        #    "^.{5}[^pausgrd]",
        #]
        #exclude_rg_filters = [
        #    "^databricks-rg"
        #]

        if( any(re.match(s, resource_group, re.IGNORECASE) for s in exclude_rg_filters) or
            any(re.match(s, name, re.IGNORECASE) for s in exclude_host_filters)):
            out="DoNothing"
        else:
            # Get powerState of VM by calling instanceView endpoint
            vm_power_state_endpoint = "https://management.azure.com{}/InstanceView?api-version=2021-03-01".format(vm['id'])
            vm_power_state_response = requests.get(vm_power_state_endpoint, headers=headers)
            if vm_power_state_response.status_code != 200:
                raise Exception("Failed to get PowerState information for VM {}".format(name))
            vm_power_state = vm_power_state_response.json()['statuses'][1]['displayStatus']
            if vm_power_state == "VM running":
                # Get Ip Address by calling nic_endpoint
                nic_id = vm["properties"]["networkProfile"]["networkInterfaces"][0]["id"]
                nic_endpoint = "https://management.azure.com{}?api-version=2022-09-01".format(nic_id)
                response = requests.get(nic_endpoint, headers=headers)
                if response.status_code != 200:
                    raise Exception("Failed to get NIC information for VM {}".format(name))
                nic = response.json()
                ip_address = nic["properties"]["ipConfigurations"][0]["properties"]["privateIPAddress"]
                # Group VMs by OS type
                if os_type == "windows":
                    inventory["IG_{}_windows".format(subscription_name)]["hosts"].append(name)
                    ansible_host = name + ".aiaazure.biz"
                elif os_type == "linux":
                    inventory["IG_{}_linux".format(subscription_name)]["hosts"].append(name)
                    ansible_host = ip_address
                inventory["_meta"]["hostvars"][name] = {
                        "aia_subscription": subscription_name,
                        "aia_subscription_id": subscription_id,
                        "ansible_host": ansible_host,
                        "availability_zone": availability_zone,
                        "default_inventory_hostname": name,
                        "location": location,
                        "name": name,
                        "vm_power_state": vm_power_state,
                        "private_ipv4_addresses": [
                            ip_address
                        ],
                        "provisioning_state": provisioning_state,
                        "public_dns_hostnames": [],
                        "public_ipv4_addresses": [],
                        "resource_group": resource_group,
                        "resource_type": resource_type
                }

    return json.dumps(inventory, indent=4)

if __name__ == "__main__":
    # Replace "your_resource_group_name" with the actual name of your resource group
    resource_group_name = 'RG-SG01-SEA-P-PROPHET'
    print(get_azure_vms())
