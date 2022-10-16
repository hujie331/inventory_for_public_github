import requests
import json
import sys
import signal
import os
import time


signal.signal(signal.SIGPIPE, signal.SIG_DFL)  # IOError: Broken pipe
signal.signal(signal.SIGINT, signal.SIG_DFL)  # KeyboardInterrupt: Ctrl-C


print()
print()
print('^' * 30)
# os.system('find /home/jhu/PycharmProjects/netmiko/device-group/* |sed "s#.*/##"')
# os.system('echo "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"')
# the following 2 lines are disabled, the device_group is hardcoded in the 3rd line
# device_group = input("Please select what device-group you want to backup \n\ndevice-group: ")
# dev_grp = '/home/jhu/PycharmProjects/netmiko/device-group/' + device_group
# dev_grp = '/home/jhu/PycharmProjects/netmiko/device-group/sjca-spare'
dev_grp = '/home/jhu/PycharmProjects/inventory/inventory_lab1a1b_juniper.json'

os.system('clear')
payload={}
headers = {
    'A...': '......',
    'Accept': 'text/plain',
    'Content-Type': 'application/xml'
}


def print_one_by_one(text):
  sys.stdout.write("\r " + " " * 60 + "\r")
  sys.stdout.flush()
  for c in text:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.01)


with open(dev_grp) as dev_file:
    devices = json.load(dev_file)

for device in devices:
    print_one_by_one('~' * 80)
    print()
    print('Connecting to device:', device['ip address'])
    url = f"http://{device['ip address']}:3000/rpc/get-configuration"
    response = requests.request("GET", url, headers=headers, data=payload)
    filename = device['hostname'] + '.cfg'
    time.sleep(2)
    print()
    print()
    with open(filename, 'w') as out_file:
        out_file.write(response.text)
    print()
    print('"' + filename + '"' + ' has been saved')


# folder = 'cfg_bk_for_' + device_group
folder = 'cfg_bk_for_' + 'lab1a1b'
folder_absolute_path = f'/home/jhu/PycharmProjects/"{folder}"'
os.system('mkdir %s 2>>confback.log' %(folder_absolute_path))
os.system('mv *.cfg %s' %(folder_absolute_path))
print()
print_one_by_one('~' * 80)
print()
print_one_by_one(f'All cfg-bk files have been saved in the folder {folder_absolute_path}\n\n')
