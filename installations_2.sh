#!/bin/sh

# Install Ansible
sudo -H pip install gitpython
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt-get update
sudo apt-get install ansible -y

# Install Ansible modules
ansible-galaxy install Juniper.junos,1.4.3

rm -rf ~/Contrail_Automation

sudo -H pip install jmespath
