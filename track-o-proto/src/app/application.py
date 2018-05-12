from app.firebase.firebase_connector import get_users

userId = "f03f6cc7-6983-4a40-9a6c-d7f4e5174ad3"

def go_for_it_girl(argv):
    print("hello world. - " + userId)
    get_users()