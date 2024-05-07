from datetime import datetime
from datetime import timedelta
from flight_search import FlightSearch
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager


today = datetime.now().strftime("%Y-%m-%d")
date1 = datetime.strptime(today, "%Y-%m-%d")
add_day = (date1 + timedelta(days=1))
tomorrow = str(add_day).split()[0]
tomorrow_for_adding = datetime.strptime(today, "%Y-%m-%d")
sheets_data = DataManager().get_data()

cheap_flights_dict = {}

for city in range(len(sheets_data)):
    city_name = sheets_data[city]["city"]
    city_code = sheets_data[city]["iataCode"]
    city_price = sheets_data[city]["lowestPrice"]
    cheap_flights_dict = {}
    notification = NotificationManager()
    print(city_name)
    for day in range(183):
        add_day = (tomorrow_for_adding + timedelta(days=day))
        new_day = str(add_day).split()[0]
        flight_search_data = FlightSearch().flight_get_request(city_code, tomorrow)
        print(day)
        for flight in range(len(flight_search_data)):
            flight_data = FlightData(flight_search_data, flight)
            flight_price = flight_data.price
            if flight_price < city_price:
                cheap_flights_dict = {
                    "iata_departure": flight_data.iata_departure,
                    "iata_arrival": flight_data.iata_arrival,
                    "departure_time": flight_data.time_departure,
                    "arrival_time": flight_data.time_arrival,
                    "price": flight_data.price,
                    "city_name": city_name
                }
                city_price = flight_price
                print(cheap_flights_dict)
    if len(cheap_flights_dict) > 0:
        notification.populate_text(cheap_flights_dict)
        notification.send_notification()


#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
