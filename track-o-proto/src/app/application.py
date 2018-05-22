from app.firebase.firebase_connector import get_user_by_id, get_users, update_connectionStatus_by_id
from app.models.user import User
from app.ble.bluetooth_scanner import scan

user_id = "5ae8a782b7340c1e60ae9f32"

def go_for_it_girl(argv):
    print("Monitoring user with ID: " + user_id)

    user_json = get_user_by_id(user_id)

    print(user_json)

    if user_json:
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

        #update_connectionStatus_by_id(user_id, user.beacons[0].mac_address, 5)

        scan(user.beacons[0].mac_address)

    else:
        print("User with ID '" + user_id + "' not found in the database.")
    