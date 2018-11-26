 #!/usr/bin/python
import json
import requests
from requests.auth import HTTPBasicAuth


# Define variables needed
username = raw_input("Username: ")
password = raw_input("Password: ")
tower = raw_input("Tower Server:")
auth = HTTPBasicAuth(username, password)
verify = False
headers = {
    "Content-Type": "application/json",
    }
# Url to GET list of all inventories in Ansible Tower
url_inventories = 'https://' + tower + '/api/v2/inventories/'
#define Set to register all hosts
hosts = set()

# Function to list all inventories in Ansible Tower
def list_inventories(url_inventories, auth, headers, verify):
    response = requests.get(url_inventories,headers = headers,auth=auth, verify = verify)
    ids = json.loads(response.content)
    return ids

# Function to get all hosts for each inventory in Ansible Tower
def get_data(url_hosts, auth, headers, verify):
    response = requests.get(url_hosts, headers=headers, auth=auth, verify=verify)
    json_response = json.loads(response.content)
    try:
        for name in json_response['results']:
            host = name['name']
            hosts.add(host)
        return hosts
    except:
        print('Inventory is empty')

ids = list_inventories(url_inventories, auth, headers, verify)

for id in ids['results']:
    url_hosts = url_inventories + str(id['id']) + '/hosts/'
    host = get_data(url_hosts, auth, headers, verify)
    print(hosts)

print len(hosts)
