import simplejson as json
from app.models.antenna import Antenna
from app.models.beacon import Beacon

class User():
    id = ""
    name = ""
    antennas = []
    beacons = []

    def __init__(self, json_content):
        parsed_json = json.loads(json_content)

        # Parse user information:
        self.id = parsed_json['id']
        self.name = parsed_json['name']

        # Parse antennas:
        parsed_antennas = parsed_json['antennas']

        for a in parsed_antennas:
            new_antenna = Antenna(a['id'])
            self.antennas.append(new_antenna)

        # Parse beacons:
        parsed_beacons = parsed_json['beacons']

        for b in parsed_beacons:
            new_beacon = Beacon(b['antennaId'], b['connectionStatus'], b['macAddress'])
            self.beacons.append(new_beacon)
