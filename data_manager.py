import requests


class DataManager:
    def __init__(self):
        self.data_sheet = {}

    def get_data(self):
        response = requests.get("https://api.sheety.co/42590b54a1ac71c7ac63510780eea096/flightDeals/prices")
        data = response.json()
        self.data_sheet = data["prices"]
        return self.data_sheet

    def update_data(self):
        for data in self.data_sheet:
            row_data = {
                "price": {
                    "iataCode": data["iataCode"]
                }
            }
            response = requests.put(f"https://api.sheety.co/42590b54a1ac71c7ac63510780eea096/flightDeals/prices/{data['id']}",
                                    json=row_data)
            print(response.text)

    def get_users(self):
        response = requests.get("https://api.sheety.co/42590b54a1ac71c7ac63510780eea096/flightDeals/users")
        return response.json()
