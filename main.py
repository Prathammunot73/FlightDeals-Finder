# Pretty Print module for neatly displaying dictionaries, lists, and JSON data.
from pprint import pprint
import requests_cache
from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

#--cache api responses for 1 hour to reduce api calls and save the free request limit,except sheety requests
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co":requests_cache.DO_NOT_CACHE,
        "*":3600,
    }
)

#--read flight destination data from sheety--
data_manager=DataManager()
sheet_data=data_manager.get_destination_data()
#pprint(sheet_data)
flight_search=FlightSearch()
#create an instance of NOtificationManager
notification_manager=NotificationManager()

#--set the dates--
tomorrow=datetime.now()+ timedelta(days=1)
six_month_from_today=datetime.now()+ timedelta(days=(6*30))
ORIGIN_CITY_IATA="LHR" #london heathrow

#--find cheap flights--
for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights=flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: GBP {cheapest_flight.price}")

    #--search for indirect flight if N/A---
    if cheapest_flight.price== "N/A":
        print(f"No direct flight to {destination['city']}. Looking for indirect flight...")
        stopover_flights=flight_search.check_flights(
            ORIGIN_CITY_IATA,
            destination["iataCode"],
            from_time=tomorrow,
            to_time=six_month_from_today,
            is_direct=False
        )
        cheapest_flight=find_cheapest_flight(stopover_flights,return_date=six_month_from_today.strftime("%Y-%m-%d"))
        print(f"Cheapest indirect flight price is: GBP {cheapest_flight.price}")

        #send sms & whatsapp msg
        message = (
            f"✈️ Low Price Alert!\n\n"
            f"Only GBP {cheapest_flight.price}\n"
            f"From: {cheapest_flight.origin_airport}\n"
            f"To: {cheapest_flight.destination_airport}\n"
            f"Departure: {cheapest_flight.out_date}\n"
            f"Return: {cheapest_flight.return_date}"
        )

        notification_manager.send_sms(message)

        notification_manager.send_whatsapp(message)