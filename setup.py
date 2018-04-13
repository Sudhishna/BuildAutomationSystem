import subprocess
import sys
import getpass
import os
import time

if sys.stdin.isatty():
    print("Enter details")
    print("***********************************")
    print("CONTRAIL HOST:")
    jnprusername = input("Username: ")
    jnprpassword = getpass.getpass("Password: ")
    hostip = input("IP Address: ")
    miface = input("Management Interface: ")
    print("FILE SERVER:")
    fileserver = input("IP Address: ")
else:
    jnprusername = sys.stdin.readline().rstrip()
    jnprpassword = sys.stdin.readline().rstrip()
    hostip = sys.stdin.readline().rstrip()
    fileserverip = sys.stdin.readline().rstrip()
    miface = sys.stdin.readline().rstrip()
    
MIFACE = miface
DEV_USER = jnprusername
PW = jnprpassword
VM_USER = getpass.getuser()
SSH_KEYGEN_DIR = "~/.ssh"

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
    
def populate_ips(devInfo="Info.txt"):
    with open(devInfo, 'w') as f:
        f.write(hostip)
        f.write(fileserver)
        
print("\n\n      ########  Making initial Installations  ########")
subprocess.call(['./installations_1.sh'])

populate_ips()
line_prepender("/etc/apt/sources.list", "deb http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main")

print("\n\n      ########  Installing Ansible and its modules  ########")
subprocess.call(['./installations_2.sh'])

if not os.path.exists(SSH_KEYGEN_DIR):
    os.makedirs(SSH_KEYGEN_DIR)

subprocess.call(['python3','setup-config.py',DEV_USER,PW,MIFACE])

