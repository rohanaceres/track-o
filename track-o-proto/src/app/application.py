from app.firebase.firebase_connector import get_username_by_id, get_users

userId = "5ae8a782b7340c1e60ae9f32"

def go_for_it_girl(argv):
    print("Monitoring user with ID: " + userId)

    #while (True):
    get_username_by_id(userId)
    #get_users()