from app.firebase.firebase_connector import get_all
from app.ble.bluetooth_scanner import scan
import time

def go_for_it_girl(argv):
    print("Start monitoring.")

    while (True):
        scan()
        time.sleep(1)
    