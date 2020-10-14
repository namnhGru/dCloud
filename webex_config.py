import requests
from functools import reduce
from requests.auth import HTTPBasicAuth
import json

BASE_URL = 'https://api.ciscospark.com/v1/'
WEBEX_API_KEY = 'NmZkMDlmNWQtZGZkMi00M2VjLThhNDctZjAxOTdjYmQ5NTZhMzhmYTkyMWQtYTVh_PF84_consumer'
authorization_hdr = 'Bearer {}'.format(WEBEX_API_KEY)
hdr = {
  'Authorization': authorization_hdr, 
  'Content-Type': 'application/json'
}

def createRooms(title):
  data = json.dumps({'title': title})
  url = '{}rooms'.format(BASE_URL)
  resp = requests.post(url, data=data, headers=hdr, verify=False)  
  return resp.json()

def listRooms():
  url = '{}rooms'.format(BASE_URL)
  resp = requests.get(url, headers=hdr, verify=False)  
  return resp.json()

def reduceToId(x,y):
  x.append(y['id'])
  return x

def getAllRoomID():
  rooms = listRooms()['items']
  roomsID = reduce(lambda x,y: reduceToId(x,y), rooms, [])
  return roomsID

def getRoomDetail(id):
  url = '{}rooms/{}'.format(BASE_URL, id)
  resp = requests.get(url, headers=hdr, verify=False)  
  return resp.json()

def updateRoom(id, data):
  url = '{}rooms/{}'.format(BASE_URL, id)
  resp = requests.put(url, data=data, headers=hdr, verify=False)  
  return resp.json()

def deleteRoom(id):
  url = '{}rooms/{}'.format(BASE_URL, id)
  resp = requests.post(url, headers=hdr, verify=False)  
  return resp.json()

def postMessage(roomId, text):
  url = 'https://webexapis.com/v1/messages'
  data = json.dumps({'roomId': roomId, 'text': text})
  resp = requests.post(url, data=data, headers=hdr, verify=False)
  return resp.json()