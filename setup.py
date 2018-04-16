import subprocess
import sys
import getpass
import os
import time

with open("Info.txt") as f:
    hostip,fileserverip = f.readlines()
    f.close()
    
yes = {'yes','y',''}
no = {'no','n'}

print("***********************************")
print("      BUILD AUTOMATION SYSTEM"
print("***********************************")
print("Populating content from Info.txt...")
print("")
print("FILE SERVER")
print("IP Address: " + fileserverip)
print("CONTRAIL HOST")
print(" IP Address: " + hostip)
print("***********************************")
print("***********************************")
print("Confirm above details (Y?N) ? ")
while True:
    choice = raw_input().lower()
    if choice in no:
        print ("Provide ip addresses in Info.txt")
        print ("First line: Contrail host ip")
        print ("Second line: File Server ip")
        sys.exit()
    elif choice in yes:
        break
    else:
        print ("Enter a valid choice : y/n "
                    
jnprusername = "root"
if sys.stdin.isatty():
    jnprpassword = getpass.getpass("Enter Contrail Host Root Password: ")     
else:
    jnprpassword = sys.stdin.readline().rstrip()
        
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
        
print("\n\n      ########  Making initial Installations  ########")
subprocess.call(['./installations_1.sh'])

line_prepender("/etc/apt/sources.list", "deb http://ppa.launchpad.net/ansible/ansible/ubuntu xenial main")

print("\n\n      ########  Installing Ansible and its modules  ########")
subprocess.call(['./installations_2.sh'])

if not os.path.exists(SSH_KEYGEN_DIR):
    os.makedirs(SSH_KEYGEN_DIR)

subprocess.call(['python3','setup-config.py',DEV_USER,PW])
