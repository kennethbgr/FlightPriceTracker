import os
import flight_data
from twilio.rest import Client
import data_manager
import smtplib

TWILIO_ACCT_SID = os.environ['TWILIO_ACCT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
TWILIO_PHONE = os.environ['TWILIO_PHONE']

MY_EMAIL = os.environ['MY_EMAIL']
MY_PASSWORD = os.environ['MY_PASSWORD']
MY_PHONE = os.environ['MY_PHONE']

class NotificationManager:
    def __init__(self):
        self.flight_class = flight_data.FlightData()
        self.data_man = data_manager.DataManager()
        self.lowest_price = 0
        self.current_price = 0

    def compare_prices(self, current_price: int, data:dict):
        self.lowest_price = data["lowestPrice"]
        self.current_price = current_price
        if self.current_price < self.lowest_price:
            return True
        else:
            return False

    def send_txt(self, text: str, link: str):
        client = Client(TWILIO_ACCT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            body=f"Low price alert!\n{text}\n{link}",
            from_=TWILIO_PHONE,
            to= MY_PHONE, )
        print(message.status)

    def send_email(self, text: str, emails:list, link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=emails,
                                msg=f"Subject: New Low Price Alert\n\n{text}\n{link}")
