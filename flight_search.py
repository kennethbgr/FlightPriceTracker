import os
import requests

FLIGHT_QUERY_ENDPOINT = os.environ['FLIGHT_QUERY_ENDPOINT']
FLIGHT_SEARCH_API = os.environ['FLIGHT_SEARCH_API']

flight_header = {
    "apikey": FLIGHT_SEARCH_API,
}


class FlightSearch:
    def replace_iata(self, data:dict):
        city = data['city']
        flight_params = {
            "term": city,
        }
        response = requests.get(url=FLIGHT_QUERY_ENDPOINT, params=flight_params, headers=flight_header)
        response.raise_for_status()
        iata_value = response.json()["locations"][0]["code"]
        return iata_value



