import requests
import os
SHEETY_PRICES_ENDPOINT = "YOUR_SHEETY_PRICES_ENDPOINT"
SHEETY_USERS_ENDPOINT="YOUR_SHEETY_USERS_ENDPOINT"
BEARER = os.environ["YOUR_API_BEARER_SHEETY"]

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.headers={
    "Authorization": f"Bearer {BEARER}",
    "Content-Type": "application/json"
  }

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=self.headers,
                json=new_data
            )
            response.raise_for_status()
    def get_user_data(self):
        response=requests.get(url=SHEETY_USERS_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        users=response.json()['users']
        # print(users)
        return users
