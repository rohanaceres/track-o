import pyrebase

config = {
  "apiKey": "AIzaSyDKnody294Y3WOawF9X_OaerU554P_coQM",
  "authDomain": "track-o-proto.firebaseapp.com",
  "databaseURL": "https://track-o-proto.firebaseio.com",
  #projectId: "track-o-proto",
  "storageBucket": "track-o-proto.appspot.com",
  "serviceAccount":"/home/rohanaceres/Workspace/ble/track-o/track-o-proto/src/app/firebase/auth/track-o-proto-firebase-adminsdk-nnnsd-8e02e250cb.json"
  #messagingSenderId: "730229429000"
}

db = pyrebase.initialize_app(config).database()

def get_users():
  users = db.child("users").get()
  print(users.val())

def get_username_by_id(userId):
  all_users = db.child("users").child(userId).get().val()
  print(all_users) # {name": "Mortimer 'Morty' Smith"}


