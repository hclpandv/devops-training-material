## Step By Step

- Install Ubuntu on your computer.
- Install Virtualbox
- Install a Ubuntu server inside virtualbox.
- Install Apache, PHP, MySQL inside the server
- Install WordPress on the server and make it work.
- Now add Nginx as a reverse proxy in front of it.
- Now create another server and install just MySQL on it.
- Dump the MySQL database from the first server and restore it on the new one.
- On the old server configure WordPress to use the database on the new server instead of the database on the old one.
- Uninstall the MySQL from the old server.
- Now create another server
- Install Nginx on it.
- Configure this new server to be a reverse proxy to the old one (pointing to Apache).
- Now remove Nginx from the old Server.
- Now install another server.
- Install NFS on it.
- Mount the NFS on the old server.
- Move your WordPress files to the NFS volume on the old server.
- Make Apache read the Files on the NFS volume.
- Now install another server
- Install Apache + PHP on it.
- Mount the NFS server and make Apache read the Files from NFS.
- Check to see if WordPress is working on this server.
- Now configure Nginx to be a reverse proxy to both Apache severs.
Congratulations, you put up a full, web HA enabled, escalable, web stack.
- Now, re-do the above using Ansible to configure the servers, fetch the WordPress codebase from GitHub and restoring the database dump (Hint: you can keep the database dump for now together with your Ansible files).
Congratulations, you made your first system using configuration management.
- Now, do the same using Ansible to *provision* AND configure the servers.
Congratulations, now you know how to provision AND configure a server stack using configuration management system automation.
- Now, refactor your Ansible automation to do the same, but on provision on AWS instead of Virtualbox.
Congratulations, your first cloud based web-stack.
- Now refactor your Ansible automation codebase to do the same but restoring the database dump from S3.
Congratulations, now you know how to restore dumps from a reliable, world available, object storage.
- Now, refactor your Ansible automation to do the same but using EFS instead of your NFS server.
Congratulations, your first Ansible provisioning using a AWS resource.
- Now refactor your Ansible codebase to do the same but using ELBs instead of the Nginx reverse proxy.
Congratulations, now you removed one single point of failure from your web-stack.
- Now refactor your Ansible codebase to do the same but replacing the MySQL database server by a RDS.
Congratulations, now you removed the remaining bottleneck of your web-stack.
- Now refactor your Ansible automation codebase to do the same but using Packer generated Golden Images + AutoScale Groups + Launch Configuration.
Congratulations, now you have a self-healing, auto-scale enabled web-stack.
If you reach this point, let me know... We may be hiring! 😊
PS: This cover the basic concepts of cloud computing, system automation, high availability and web application hosting.
If you know this to add Docker, CI/CD pipelines, Kubernetes, etc is a matter of just replacing parts of it.
It's a solid ground work that can teach you a lot.
