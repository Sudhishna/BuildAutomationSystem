#!/bin/sh

# Accept the SSH Keys
ssh-keygen -R 10.10.7.205
ssh-keyscan -H 10.10.7.205 >> ~/.ssh/known_hosts

ssh-keygen -R 10.10.7.202
ssh-keyscan -H 10.10.7.202 >> ~/.ssh/known_hosts

