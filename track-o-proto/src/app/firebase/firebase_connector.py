import simplejson as json
from collections import OrderedDict
import firebase_admin
from firebase_admin import credentials, db

DATABASE_URL = "https://track-o-proto.firebaseio.com"
SERVICE_ACCOUNT = "/home/atla/Workspace/track-o/track-o-proto/src/app/firebase/auth/firebase-key.json"

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

def get_users():
  return root.child("users").get()

def get_user_by_id(user_id):
  user = root.child("users").child(user_id).get()
  user_json = json.dumps(user)
  return user_json

def update_connectionStatus_by_id(user_id, beacon_mac_address, new_connection_status):
  old_beacon = root.child("users").child(user_id).child("beacons").order_by_child("macAddress").equal_to(beacon_mac_address).limit_to_first(1).get()
  old_beacon = json.loads(json.dumps(old_beacon))
  old_beacon = old_beacon[beacon_mac_address]
  
  new_beacon = old_beacon
  new_beacon['connectionStatus'] = new_connection_status
  
  root.child("users").child(user_id).child("beacons").child(beacon_mac_address).update(new_beacon)