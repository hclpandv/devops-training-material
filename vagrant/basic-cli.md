[<<Back](index.md)
## Basic Commands

```bash
# Spin up the Vagrant VM
vagrant up
vagrant --no-provision
# Provision Only
vagrant provision
# halt - Stops he vagrant machine | destroy - Stops and deletes all traces of the vagrant machine 
# suspend - Suspends the vagrant machine. saves current state.
# resume - Resumes a suspended machine | reload - restarts and loads new Vagrantfile config
vagrant destroy -f # -f for force i.e. no confirmation msg
vagrant destroy <VM Name> # as defined in Vagrantfile

# IMPORTANT
vagrant global-status
# Output as Below
id       name         provider   state    directory
---------------------------------------------------------------------------------------------
acc7824  example-box  virtualbox running  C:/Users/vpandey/host-manager-vagrant-test
1069eee  server-2     virtualbox running  C:/Users/vpandey/vagrant-test-box-2
2ace0a0  drupalvm     virtualbox running  C:/Users/vpandey/drupal-vm
3072a70  drupalvm     virtualbox running  C:/Users/vpandey/pipe-line-demo
c42b2bc  default      virtualbox running  C:/Users/vpandey/viki-general-test-box
```
