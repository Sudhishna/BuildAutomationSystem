# BuildAutomationSystem
Steps:
1. cd BuildAutomationSystem
2. Enter the contrail host ip and file server ip in the file Info.txt
3. Run python3 setup.py
4. After this script is successfully run, next step is to start provisioning the contrail host. Enter the Contrail_Automation folder which was cloned by the python script
5. Run './Contrail-Install.sh'  for the setup -> Contrail 4.1 on Ubuntu 16.04 BMS, OR
6. Run 'bash Contrail5-Centos-Install.sh' for the setup -> Contrail 5.0 on Centos 7.4 BMS
