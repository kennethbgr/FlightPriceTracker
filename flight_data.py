import os
import requests
import datetime as dt

FLIGHT_SEARCH_ENDPOINT = os.environ['FLIGHT_SEARCH_ENDPOINT']
FLIGHT_SEARCH_API = os.environ['FLIGHT_SEARCH_API']

flight_header = {
    "apikey": FLIGHT_SEARCH_API,
}

class FlightData:
    def __init__(self):
        self.price = 0
        self.departure_airport_code = "RDU"
        self.departure_city = "North Carolina"
        self.currency = "USD"
        self.day_tomorrow = (dt.datetime.now()+dt.timedelta(1)).strftime("%d/%m/%Y")
        self.day_six_months = (dt.datetime.now()+dt.timedelta(181)).strftime("%d/%m/%Y")
        self.return_from = (dt.datetime.now()+dt.timedelta(8)).strftime("%d/%m/%Y")
        self.return_to = (dt.datetime.now()+dt.timedelta(29)).strftime("%d/%m/%Y")
        self.airlines = ""
        self.flight_num = 0
        self.arrival_city = ""
        self.airport_to = ""
        self.seats_available = 0
        self.outbound_date = ""
        self.inbound_date = ""
        self.stop_overs = 0
        self.via_city = " "

    def search_flight_data(self, data: dict):
        iata_code = data['iataCode']
        flight_search_params = {
            "fly_from": self.departure_airport_code,
            "fly_to": iata_code,
            "date_from": self.day_tomorrow,
            "date_to": self.day_tomorrow,
            "return_from": self.return_from,
            "return_to": self.return_to,
            "curr": self.currency,
            "max_stopovers": 0,
        }
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=flight_search_params, headers=flight_header)
        response.raise_for_status()
        try:
            json_response = response.json()["data"][0]
        except IndexError:
            flight_search_params["max_stopovers"] = 3
            response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=flight_search_params, headers=flight_header)
            response.raise_for_status()
            try:
                json_response = response.json()["data"][0]
            except IndexError:
                return None
            else:
                self.price = json_response["price"]
                self.arrival_city = json_response["cityTo"]
                self.seats_available = json_response["availability"]["seats"]
                self.outbound_date = json_response["route"][0]["local_departure"].split("T")[0]
                self.inbound_date = json_response["route"][-1]["local_arrival"].split("T")[0]
                self.airport_to = json_response["flyTo"]
                link = f"https://www.google.com/travel/flights?hl=en#flt={self.departure_airport_code}.{self.airport_to}." \
                       f"{self.outbound_date}*{self.airport_to}.{self.departure_airport_code}.{self.inbound_date}"
                return f"Price: ${self.price}\nDeparture city: {self.departure_city}-{self.departure_airport_code}\n" \
                       f"City to: {self.arrival_city}-{self.airport_to}\nSeats available: {self.seats_available}\n" \
                       f"From: {self.outbound_date}\nTo: {self.inbound_date}\n", self.price, link
        else:
            self.price = json_response["price"]
            self.arrival_city = json_response["cityTo"]
            self.seats_available = json_response["availability"]["seats"]
            self.outbound_date = json_response["route"][0]["local_departure"].split("T")[0]
            self.inbound_date = json_response["route"][-1]["local_arrival"].split("T")[0]
            self.airport_to = json_response["flyTo"]
            link = f"https://www.google.com/travel/flights?hl=en#flt={self.departure_airport_code}.{self.airport_to}." \
                   f"{self.outbound_date}*{self.airport_to}.{self.departure_airport_code}.{self.inbound_date}"
            return f"Price: ${self.price}\nDeparture city: {self.departure_city}-{self.departure_airport_code}\n" \
                   f"City to: {self.arrival_city}-{self.airport_to}\nSeats available: {self.seats_available}\n" \
                   f"From: {self.outbound_date}\nTo: {self.inbound_date}\n", self.price, link


