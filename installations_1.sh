#!/bin/sh

# To get the latest package lists 
sudo apt-get update && sudo apt-get upgrade -y

# Install Python
sudo apt-get install python-pip python-dev libxml2-dev libxslt-dev libssl-dev libffi-dev -y
sudo apt-get install libpython3-dev libpython3.5-dev python3-dev python3-pip python3-setuptools python3-wheel python3.5-dev -y

# Upgrade pip
sudo -H pip install --upgrade pip
sudo -H pip3 install --upgrade pip

# Install Juniper Libraries
sudo -H pip2 install junos-eznc
sudo -H pip2 install jxmlease
sudo -H pip3 install junos-eznc
sudo -H pip3 install jxmlease

