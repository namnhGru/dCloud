import requests
from functools import reduce
from requests.auth import HTTPBasicAuth

MERAKI_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'
def get_networks_info():
    """
    Building out Auth request. Using requests.post to make a call to the Auth Endpoint
    """
    url = 'https://api.meraki.com/api/v0/organizations/' # Endpoint URL
    hdr = {
      'X-Cisco-Meraki-API-Key': MERAKI_API_KEY,
      'Content-Type': 'application/json'
    }
    resp = requests.get(url, headers=hdr, verify=False)  # Make the POST Request
    return resp.json()# Create a return statement to send the token back for later use 

def reducedToList(x, y, yAttr):
  x.append(y[yAttr])
  return x

def getNetworkIDLists():
  networksInfo = get_networks_info()
  print(networksInfo)
  result = reduce(lambda x,y: reducedToList(x, y, yAttr='id'), networksInfo, [])
  print(result)
  return result
  