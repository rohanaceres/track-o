from app.firebase.firebase_connector import get_username_by_id, get_users
from app.models.user import User

userId = "5ae8a782b7340c1e60ae9f32"

def go_for_it_girl(argv):
    print("Monitoring user with ID: " + userId)

    #while (True):
    user_json = get_username_by_id(userId)
    user = User(user_json)
    
    print("User name: " + user.name)
    print("User ID: " + user.id)
    print("----------------")

    count = 1
    for antenna in user.antennas:
        print("Antenna #" + str(count) + ": " + antenna.id)
        print("----------------")

    count = 1
    for beacon in user.beacons:
        print("Beacon #" + str(count) + ": " + beacon.mac_address)
        print("Status: " + str(beacon.connection_status))
        print("Antenna ID: " + beacon.antenna_id)
        print("----------------")
    