import simplejson as json
from collections import OrderedDict
import firebase_admin
from firebase_admin import credentials, db
import array
import logging

DATABASE_URL = "https://track-o-proto.firebaseio.com"
SERVICE_ACCOUNT = "/home/atla/Workspace/firebase-key.json"

config = {
  "apiKey": "AIzaSyDKnody294Y3WOawF9X_OaerU554P_coQM",
  "authDomain": "track-o-proto.firebaseapp.com",
  "databaseURL": DATABASE_URL,
  "projectId": "track-o-proto",
  "storageBucket": "track-o-proto.appspot.com",
  "serviceAccount": SERVICE_ACCOUNT,
  "messagingSenderId": "730229429000"
}

cred = credentials.Certificate(SERVICE_ACCOUNT)
firebase_admin.initialize_app(cred, 
{
  "databaseURL": "https://track-o-proto.firebaseio.com"
})
print("Firebase initialized.")

root = db.reference()

def get_all():
  return root.get()

def add_one(beacon):
  beacons = list()
  firebaseData = root.get()
  
  if firebaseData is None:
    beacons.append(beacon)
    root.set(beacons)
  else:
   beacons.extend(firebaseData)
   beacons.append(beacon)
   root.set(beacons)