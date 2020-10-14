import requests
from functools import reduce
from requests.auth import HTTPBasicAuth

MERAKI_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
hdr = {
  'X-Cisco-Meraki-API-Key': MERAKI_API_KEY,
  'Content-Type': 'application/json'
}
def get_networks_info():
    url = 'https://api.meraki.com/api/v0/organizations/' # Endpoint URL
    resp = requests.get(url, headers=hdr, verify=False)  # Make the POST Request
    return resp.json()# Create a return statement to send the token back for later use 

def reducedToList(x, y, yAttr):
  x.append(y[yAttr])
  return x

def getOrganizationIDLists():
  networksInfo = get_networks_info()
  result = reduce(lambda x,y: reducedToList(x, y, yAttr='id'), networksInfo, [])
  return result

def getOrganizationNetworks(organizationID):
  url = 'https://api.meraki.com/api/v0/organizations/{}/networks'.format(organizationID)
  resp = requests.get(url, headers=hdr, verify=False) 
  return resp.json() 

def getOrganizationDevices(networkID):
  url = 'https://api.meraki.com/api/v0/networks/{}/devices'.format(networkID)
  resp = requests.get(url, headers=hdr, verify=False) 
  return resp.json() 
  
def getNetworkInfo(networkID):
  url = 'https://api.meraki.com/api/v0/networks/{}'.format(networkID)
  resp = requests.get(url, headers=hdr, verify=False) 
  return resp.json() 

def getDeviceInfo(networkID, serial):
  url = 'https://api.meraki.com/api/v0/networks/{}/devices/{}'.format(networkID, serial)
  resp = requests.get(url, headers=hdr, verify=False) 
  return resp.json() 

def getSSIDInfo(networkID):
  url = 'https://api.meraki.com/api/v0/networks/{}/ssids'.format(networkID)
  resp = requests.get(url, headers=hdr, verify=False) 
  return resp.json() 
