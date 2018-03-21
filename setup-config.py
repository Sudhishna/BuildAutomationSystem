import subprocess
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
import sys
import getpass
import git
import os
import time

jnprusername = str(sys.argv[1])
jnprpassword = str(sys.argv[2])

DEV_USER = jnprusername
PW = jnprpassword
VM_USER = getpass.getuser()
SSH_KEYGEN_DIR = "~/.ssh"
HOME_DIR = "/root/"

def line_prepender(filename, line):
    #with os.popen(filename, 'w').write(PW) as f:
    with open(filename, 'rt') as f:
        content = f.read()
        f.seek(0, 0)
        s = line.rstrip('\r\n') + '\n' + content
        with open('tempfile.tmp', 'wt') as outf:
            outf.write(s)
    command = 'sudo mv tempfile.tmp ' + filename
    os.system('echo %s|sudo -S %s' % (PW, command))

def make_executable(path):
    mode = os.stat(path).st_mode
    mode |= (mode & 0o444) >> 2    # copy R bits to X
    os.chmod(path, mode)
    
def push_key(devInfo="Info.txt"):
    """Push SSH Key to a remote server."""

    with open(devInfo, 'r') as f:
        devices = f.readlines()
        devices = [x.strip() for x in devices]

        for device in devices:
            command = "sshpass -p '" + PW + "' ssh-copy-id " + DEV_USER + "@" + device
            subprocess.call(command, shell=True)

def key_present():
    """Checks to see if there is an RSA already present. Returns a bool."""
    if "id_rsa" in os.listdir(SSH_KEYGEN_DIR):
        return True
    else:
        return False

def gen_key():
    """Generate a SSH Key."""
    if key_present():
        print("A key is already present.")
    else:
        # Genarate private key
        command = "ssh-keygen -f ~/.ssh/id_rsa -N ''"
        subprocess.call(command, shell=True)

def accept_ssh_keys(devInfo="Info.txt"):
    with open(devInfo, 'r') as f:
        devices = f.readlines()
        devices = [x.strip() for x in devices]

        accept_keys = "#!/bin/sh\n\n# Accept the SSH Keys\n"
        for device in devices:
            accept_keys += "ssh-keygen -R {}\nssh-keyscan -H {} >> ~/.ssh/known_hosts\n\n".format(device,device)
        print("{}".format(accept_keys))
        with open("/root/BuildAutomationSystem/installations_3.sh", "w") as fil:
            fil.write(accept_keys)
            fil.close()
        time.sleep(3)
        
        make_executable("/root/BuildAutomationSystem/installations_3.sh")

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

print("\n\n      ########  Clone the GIT Project Repository  ########")
git.Git(HOME_DIR).clone("https://github.com/Sudhishna/Contrail_Automation.git")
print("Contrail Ansible Project cloned")

print("\n\n      ########  Generate SSH Key  ########")
gen_key()

print("\n\n      ########  Accept the key from remote vm  ########")
accept_ssh_keys()
subprocess.call(['./installations_3.sh'])

print("\n\n      ########  Push key to the remote vm  ########")
push_key()

print("\n\n      ########  Wait for the VMs to stablize  ########")
countdown(20)

print("\n\n      #####  AUTOMATION SYSTEM IS READY  #####")
