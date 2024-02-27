import requests
import pandas as pd


class AccommodationByCommuteTime:

    def __init__(self):
        self._commute_times = None
        self.headers = {
            'Content-Type': 'application/json',
            'X-Application-Id': 'e28b04fb',
            'X-Api-Key': 'f37e5645ccd37281e510ae5637860362'
        }

        self.key_locations = []
        self.key_locations_names = []
        self.df = pd.DataFrame()

    def add_key_location(self, location_name, latitude, longitude):
        """
        this method adds a location to the class, meaning that when a commute time query is made the distance to the new location will be also calculated.

        :param location_name: the name of the key location which is important to have a reasonable drive time to.
        :param latitude: the latitude of the key location which can be found via right clicking on Google Maps.
        :param longitude: the longitude of the key location which can be found via right clicking on Google Maps.
        :return: None
        """
        self.key_locations.append({
            "id": location_name,
            "coords": {
                "lat": latitude,
                "lng": longitude
            }
        })
        self.key_locations_names.append(location_name)
        if location_name not in self.df.columns:
            self.df[location_name] = None

    def find_commute_time(self, location_name, latitude, longitude):
        """
        queries the distances and commute times, via car, to the given location.

        :param location_name: name of the location where you're thinking of moving to.
        :param latitude: the latitude of the key location which can be found via right clicking on Google Maps.
        :param longitude: the longitude of the key location which can be found via right clicking on Google Maps.
        :return:
        """
        main_location = {
            "id": location_name,
            "coords": {
                "lat": latitude,
                "lng": longitude
            }
        }

        data = {
            "locations": self.key_locations + [main_location],
            "departure_searches": [
                {
                    "id": "One-to-many Matrix",
                    "departure_location_id": f"{location_name}",
                    "arrival_location_ids": self.key_locations_names,
                    "departure_time": "2024-09-21T09:00:00Z",
                    "travel_time": 8000,
                    "properties": [
                        "travel_time",
                        "distance"
                    ],
                    "transportation": {
                        "type": "driving"
                    }
                }
            ]
        }

        # Make a post request
        response = requests.post('https://api.traveltimeapp.com/v4/time-filter',
                                 headers=self.headers,
                                 json=data)

        # # print status code
        # print(response.status_code)

        infos = response.json()['results'][0]['locations']

        #self.df.loc[location_name] = None

        for info in infos:
            info_name = info['id']
            travel_time = info['properties'][0]['travel_time']
            self.df.loc[location_name, info_name] = round(travel_time/60, 0)

        #print(self.df)



