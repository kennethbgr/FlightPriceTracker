import os
import requests

SHEETY_PRICES_ENDPOINT = os.environ['SHEETY_PRICES_ENDPOINT']
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']
SHEETY_USERS_ENDPOINT = os.environ['SHEETY_USERS_ENDPOINT']

sheety_headers = {
    "Authorization": SHEETY_TOKEN,
}


class DataManager:
    def __init__(self):
        self.response = ""

    def read_data(self):
        self.response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=sheety_headers)
        self.response.raise_for_status()
        return self.response.json()["prices"]

    def update_data(self, data: dict, index: int):
        iata_value = data['iataCode']
        sheety_params = {
            "price": {
                "iataCode": iata_value,
            }
        }
        PUT_ENDPOINT = f"{SHEETY_PRICES_ENDPOINT}/{index}"
        self.response = requests.put(url=PUT_ENDPOINT, json=sheety_params, headers=sheety_headers)
        self.response.raise_for_status()

    def read_email(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=sheety_headers)
        response.raise_for_status()
        data = response.json()['users']
        emails = [row["email"] for row in data]
        return emails


