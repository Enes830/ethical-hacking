import subprocess
import re
from itertools import zip_longest

first = subprocess.run('netsh wlan show profiles',shell = True , capture_output=True).stdout.decode()

profile_names = (re.findall("All User Profile     : (.*)\r", first))

passwords = []
names = []

for name in profile_names:
    sec = subprocess.run(f'netsh wlan show profile {name} key=clear',capture_output=True).stdout.decode()
    password = re.findall("Key Content            : (.*)\r", sec)
    name = re.findall("Name                   :(.*)\r", sec)
    passwords.append(password)
    names.append(name)
    # print(names,"-->",passwords)


list_pass = [x for x in passwords if x]

list_name = [x for x in names if x]

lists = [list_name,list_pass]

exported = zip_longest(*lists)

for wi in exported:
    print(wi[0][0],"-->",wi[1][0])