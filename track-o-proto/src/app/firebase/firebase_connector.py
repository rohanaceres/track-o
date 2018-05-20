import pyrebase
import simplejson as json
from collections import OrderedDict

config = {
  "apiKey": "AIzaSyDKnody294Y3WOawF9X_OaerU554P_coQM",
  "authDomain": "track-o-proto.firebaseapp.com",
  "databaseURL": "https://track-o-proto.firebaseio.com",
  #projectId: "track-o-proto",
  "storageBucket": "track-o-proto.appspot.com",
  "serviceAccount":"/home/atla/Workspace/track-o/track-o-proto/src/app/firebase/auth/firebase-key.json"
  #messagingSenderId: "730229429000"
}

db = pyrebase.initialize_app(config).database()

def get_users():
  users = db.child("users").get()

def get_username_by_id(userId):
  all_users = db.child("users").child(userId).get().val()
  output_dict = json.dumps(all_users)
  return output_dict


