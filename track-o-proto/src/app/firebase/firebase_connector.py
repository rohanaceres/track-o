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
  return root.child("users2").get()

def get_user_by_id(userId):
  all_users = root.child("users2").child(userId).get()
  output_dict = json.dumps(all_users)
  return output_dict


