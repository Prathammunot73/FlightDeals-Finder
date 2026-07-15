# Pretty Print module for neatly displaying dictionaries, lists, and JSON data.
from pprint import pprint
import requests_cache
from datetime import datetime,timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

# cache api responses for 1 hour to reduce api calls and save the free request limit,except sheety requests
requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co":requests_cache.DO_NOT_CACHE,
        "*":3600,
    }
)

# read flight destination data from sheety
data_manager=DataManager()
sheet_data=data_manager.get_destination_data()
pprint(sheet_data)

#set the dates
tomorrow=datetime.now()+ timedelta(days=1)
six_month_from_today=datetime.now()+ timedelta(days=(6*30))

#flight search
flight_search=FlightSearch()

flights=flight_search.check_flights(
    origin_city_code="LHR",
    destination_city_code="PNQ",
    from_time=tomorrow,
    to_time=six_month_from_today
)

# pprint(flights)

#show cheapest flight
cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
pprint(f"{sheet_data[0]['city']}: GBP {cheapest_flight.price}")

if cheapest_flight.price != "N/A" and cheapest_flight.price < sheet_data[0]["lowestPrice"]:
    pprint(f"Lower price flight found to {sheet_data[0]['city']}!")
    data_manager.update_lowest_price(sheet_data[0]["id"], cheapest_flight.price)