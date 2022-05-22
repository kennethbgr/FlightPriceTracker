import requests
import os

SHEETY_USERS_ENDPOINT = os.environ['SHEETY_USERS_ENDPOINT']
SHEETY_TOKEN = os.environ['SHEETY_TOKEN']

sheety_headers = {
    "Authorization": SHEETY_TOKEN,
}

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_verif = input("Type your email again\n")

if email != email_verif:
    print("Emails do not match, try again later")
else:
    sheety_params = {
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email,
            }
    }
    response = requests.post(url=SHEETY_USERS_ENDPOINT, json=sheety_params, headers=sheety_headers)
    response.raise_for_status()
    print(response.text)
    print("Thanks for registering! Welcome to the club!")
