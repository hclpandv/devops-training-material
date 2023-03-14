## Variables

* Terraform variables are like parameters if it is defined in variable block and does not contain `default` attribute. Then it will be prompted for the user input when you run the `terraform plan` or `terraform apply`

```
variable "location" {
  type = string
  description = "Azure Location / Region to host infra" //This is shown as hint when prompted to provide input
  default     = "westeurope"

  validation {
    condition     = var.location == "westeurope" || var.location == "northeurope"
    error_message = "Sorry, but we only accept Location as westeurop or northeurope."
  }
}
```
