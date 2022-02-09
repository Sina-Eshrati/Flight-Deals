from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import datetime

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# ------------------------------------ Main Data Using Sheety API ------------------------------------------
# data_sheet = data_manager.get_data()
#
# for row in data_sheet:
#     data = flight_search.get_iata_code(row["city"])
#     row["iataCode"] = data["locations"][0]["code"]
# print(data_sheet)
#
# data_manager.data_sheet = data_sheet
# data_manager.update_data()

# users = data_manager.get_users()
# users_email = []
# for user in users["users"]:
#     users_email.append(user["email"])

# ------------------------------------ Test Data -----------------------------------------
data_sheet = [{"city": "Bali", "iataCode": "DPS", "lowestPrice": 988, "id": 3},
              {"city": "Paris", "iataCode": "PAR", "lowestPrice": 76, "id": 2},
              {"city": "Berlin", "iataCode": "BER", "lowestPrice": 59, "id": 4},
              {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 683, "id": 5},
              {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 776, "id": 6},
              {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 133, "id": 7},
              {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 583, "id": 8},
              {"city": "New York", "iataCode": "NYC", "lowestPrice": 338, "id": 9},
              {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 366, "id": 10},
              {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 532, "id": 11}]

users_email = ['eshratisina@gmail.com', "chamanfaramir@gmail.com", "sorourisepehr@gmail.com", "mirbagherishiva@yahoo.com"]

# ----------------------------------------- Main Code -----------------------------------------------
date_from = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%d/%m/%Y")
date_to = (datetime.datetime.now() + datetime.timedelta(days=181)).strftime("%d/%m/%Y")

for data in data_sheet:
    flight_data = flight_search.check_flights(data["iataCode"], date_from, date_to)
    if flight_data is None:
        continue
    if flight_data and flight_data.price < data["lowestPrice"]:
        message = f"Low Price Alert! Only ${flight_data.price} to fly from {flight_data.departure_city}-" \
                  f"{flight_data.departure_airport} to {flight_data.destination_city}-{flight_data.destination_airport}," \
                  f" from {flight_data.out_date} to {flight_data.return_date}"
        if flight_data.stop_overs > 0:
            message += f"\nFlight has 1 stop over, via {flight_data.via_city} city."
        message += f"\nhttps://www.google.co.uk/flights?hl=en#flt={flight_data.departure_airport}.{flight_data.destination_airport}.{flight_data.out_date}*{flight_data.destination_airport}.{flight_data.departure_airport}.{flight_data.return_date}"
        for email in users_email:
            notification_manager.send_email(message, email)
        # notification_manager.send_message(message)
