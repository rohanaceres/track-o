

#!/usr/bin/python
#   File : test_beacon.py
#   Author: jmleglise
#   Date: 25-May-2016
#   Description : Test yours beacon 
#   URL : https://github.com/jmleglise/mylittle-domoticz/edit/master/Presence%20detection%20%28beacon%29/test_beacon.py
#   Version : 1.0
#

from app.ble.bluetooth_tag import BluetoothTag 

ble_tag = BluetoothTag()

import logging
import firebase_admin

# choose between DEBUG (log every information) or CRITICAL (only error)
logLevel=logging.DEBUG
#logLevel=logging.CRITICAL

#logOutFilename='/var/log/test_beacon.log'       # output LOG : File or console (comment this line to console output)


################ Nothing to edit under this line #####################################################################################

import os
import subprocess
import sys
import struct
import bluetooth._bluetooth as bluez
import time
import requests
import signal
import threading
import datetime
import random
from app.firebase.firebase_connector import upsert_by_macaddress

LE_META_EVENT = 0x3e
OGF_LE_CTL=0x08
OCF_LE_SET_SCAN_ENABLE=0x000C
EVT_LE_CONN_COMPLETE=0x01
EVT_LE_ADVERTISING_REPORT=0x02

CELL_ID = "scenario_a"

TESTBED_SAMPLES = 300

def print_packet(pkt):
    for c in pkt:
        sys.stdout.write("%02x " % struct.unpack("B",c)[0])

def packed_bdaddr_to_string(bdaddr_packed):
    return ':'.join('%02x'%i for i in struct.unpack("<BBBBBB", bdaddr_packed[::-1]))

def hci_disable_le_scan(sock):
    hci_toggle_le_scan(sock, 0x00)

def hci_toggle_le_scan(sock, enable):
    cmd_pkt = struct.pack("<BB", enable, 0x00)
    bluez.hci_send_cmd(sock, OGF_LE_CTL, OCF_LE_SET_SCAN_ENABLE, cmd_pkt)

def handler(signum = None, frame = None):
    time.sleep(1)  #here check if process is done
    sys.exit(0)   
    
def scan():
    beacon_found = False

    for sig in [signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT]:
        signal.signal(sig, handler)

    # Setup logging:
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    if "logOutFilename" in globals() :
        logging.basicConfig(format=FORMAT,filename=logOutFilename,level=logLevel)
    else:
        logging.basicConfig(format=FORMAT,level=logLevel)

    # Reset Bluetooth interface, hci0
    os.system("sudo hciconfig hci0 down")
    os.system("sudo hciconfig hci0 up")

    # Make sure device is up
    interface = subprocess.Popen(["sudo hciconfig"], stdout=subprocess.PIPE, shell=True)
    (output, err) = interface.communicate()

    # Get the output from bytes to text (UTF-8):
    output = output.decode("utf-8")

    # Check return of hciconfig to make sure it's up:
    # (This validation will only make sense if the hci0 is the only hci available.)
    if "RUNNING" in output: 
        logging.debug('Ok hci0 interface Up n running !')
    else:
        logging.critical('Error : hci0 interface not Running. Do you have a BLE device connected to hci0 ? Check with hciconfig !')
        sys.exit(1)
    
    # Define the hci number. In this case, hci0:
    devId = 0

    # Try to open connection with hci0:
    try:
        sock = bluez.hci_open_dev(devId)
        logging.debug('Connect to bluetooth device %i',devId)
    except:
        logging.critical('Unable to connect to bluetooth device...')
        sys.exit(1)

    # Gets the value of the given socket option, which can contain 14 characteres 
    # at maximum:
    old_filter = sock.getsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, 14)
    hci_toggle_le_scan(sock, 0x01)

    # Start scanning!
    print("Scanning...")

    call_count = 0
    testbed_counter = 0

    while True:
        old_filter = sock.getsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, 14)
        
        # Creates new filter:
        new_filter = bluez.hci_filter_new()
        bluez.hci_filter_all_events(new_filter)
        bluez.hci_filter_set_ptype(new_filter, bluez.HCI_EVENT_PKT)
        sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, new_filter)
        
        # Receive data from the socket (255 bytes at maximum):
        pkt = sock.recv(255)
        ptype, event, plen = struct.unpack("BBB", pkt[:3])

        # Verifies the type of the event received by the socket:
        if event == bluez.EVT_INQUIRY_RESULT_WITH_RSSI or event == bluez.EVT_NUM_COMP_PKTS or event == bluez.EVT_DISCONN_COMPLETE:
            i = 0
            
        elif event == LE_META_EVENT:
            subevent = pkt[3]
            
            #logging.info(pkt)

            pkt = pkt[4:]

            if subevent == EVT_LE_CONN_COMPLETE:
                le_handle_connection_complete(pkt)

            elif subevent == EVT_LE_ADVERTISING_REPORT:
                num_reports = pkt[0]
                report_pkt_offset = 0

                for i in range(0, num_reports):
                    macAddressSeen = packed_bdaddr_to_string(pkt[report_pkt_offset + 3:report_pkt_offset + 9])
                    
                    
                    if "0c:f3:ee:04" in macAddressSeen:
                        #logging.debug('is beacon!')
                        
                        #print "\tfullpacket: ", printpacket(pkt)
                        #print "\tUDID: ", printpacket(pkt[report_pkt_offset -22: report_pkt_offset - 6])
                        #print "\tMAJOR: ", printpacket(pkt[report_pkt_offset -6: report_pkt_offset - 4])
                        #print "\tMINOR: ", printpacket(pkt[report_pkt_offset -4: report_pkt_offset - 2])
                        #print "\tMAC address: ", packed_bdaddr_to_string(pkt[report_pkt_offset + 3:report_pkt_offset + 9])

                        #logging.debug(type(pkt))
                        #logging.debug(pkt)
                        #logging.debug(pkt[4:].decode("utf-8")) 

                        datetime = time.strftime("%Y-%m-%d %H:%M:%S")
                        logging.debug('%s, %s, %d', datetime, macAddressSeen, testbed_counter + 1)
                        distance = -1

                        testbed_counter = testbed_counter + 1

                        try:
                            upsert_by_macaddress({"cellId":CELL_ID, "dateTime":datetime, "distanceFromCell":distance, "macAddress":macAddressSeen})
                        except firebase_admin.db.ApiCallError:
                            logging.error("Error while inserting the beacon into Firebase.")

        # if testbed_counter >= TESTBED_SAMPLES:
        #     logging.debug('Test finished.')
        #     break

        sock.setsockopt(bluez.SOL_HCI, bluez.HCI_FILTER, old_filter)
        time.sleep(10 / 1000)
    
    logging.debug('------------------------------')

