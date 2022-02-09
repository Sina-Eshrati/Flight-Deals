import requests
from pprint import pprint
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "NA3bFnj-OWDlMNnl3O2aSBqLUy_DELWl"


class FlightSearch:

    def get_iata_code(self, city):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        parameters = {
            "term": city
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=parameters, headers=headers)
        return response.json()

    def check_flights(self, iata_code, date_from, date_to):
        headers = {
            "apikey": TEQUILA_API_KEY
        }
        parameters = {
            "fly_from": "LON",
            "fly_to": iata_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "USD",
            "max_stopovers": 0
        }
        response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=headers)
        try:
            cheapest_flight = response.json()["data"][0]
            # print(f"{cheapest_flight['cityTo']}: £{cheapest_flight['price']}")
        except IndexError:
            parameters["max_stopovers"] = 2
            response = requests.get(f"{TEQUILA_ENDPOINT}/v2/search", params=parameters, headers=headers)
            cheapest_flight = response.json()["data"][0]
            # print(f"{cheapest_flight['cityTo']}: £{cheapest_flight['price']}")
            return FlightData(price=cheapest_flight["price"],
                              departure_city=cheapest_flight["route"][0]["cityFrom"],
                              departure_airport=cheapest_flight["route"][0]["flyFrom"],
                              destination_city=cheapest_flight["route"][1]["cityTo"],
                              destination_airport=cheapest_flight["route"][1]["flyTo"],
                              out_date=cheapest_flight["route"][0]["local_departure"].split("T")[0],
                              return_date=cheapest_flight["route"][2]["local_departure"].split("T")[0],
                              stop_overs=1,
                              via_city=cheapest_flight["route"][0]["cityTo"])
        else:
            return FlightData(price=cheapest_flight["price"],
                              departure_city=cheapest_flight["route"][0]["cityFrom"],
                              departure_airport=cheapest_flight["route"][0]["flyFrom"],
                              destination_city=cheapest_flight["route"][0]["cityTo"],
                              destination_airport=cheapest_flight["route"][0]["flyTo"],
                              out_date=cheapest_flight["route"][0]["local_departure"].split("T")[0],
                              return_date=cheapest_flight["route"][1]["local_departure"].split("T")[0])
