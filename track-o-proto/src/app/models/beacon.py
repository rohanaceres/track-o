import simplejson as json

class Beacon():
    antenna_id = ""
    connection_status = 0
    mac_address = ""

    def __init__(self, antenna_id, connection_status, mac_address):
        self.antenna_id = antenna_id
        self.connection_status = connection_status
        self.mac_address = mac_address