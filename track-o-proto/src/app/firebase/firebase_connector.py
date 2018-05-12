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

def get_users():
    firebase = pyrebase.initialize_app(config)

    db = firebase.database()
    users = db.child("users").get()
    print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}
