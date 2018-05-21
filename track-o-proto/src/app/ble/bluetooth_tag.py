import time
import datetime
from ww import f

class BluetoothTag():
    mac_address = ""
    max_time_out = datetime.time(1, 0)
    last_time_seen = datetime.time(0, 0)
    rssid = ""

    def __str__(self):
        #return ("{\"mac_address\":\"{0}\", \"max_time_out\":\"{1}\", \"last_time_seen\":\"{2}\", \"rssid\":\"{3}}").format(self.mac_address, self.max_time_out, self.last_time_seen, self.rssid)
        print(f('mac_address:{self.mac_address}, max_time_out:{self.max_time_out}, last_time_seen:{self.last_time_seen}, rssid:{self.rssid}'))
        return (f('mac_address:{self.mac_address}, max_time_out:{self.max_time_out}, last_time_seen:{self.last_time_seen}, rssid:{self.rssid} dd'))