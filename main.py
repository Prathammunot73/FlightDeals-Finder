# Pretty Print module for neatly displaying dictionaries, lists, and JSON data.
from pprint import pprint

#pass data back to main.py to print data from main.py
from data_manager import DataManager
data_manager=DataManager()
sheet_data=data_manager.get_destination_data()
# print(sheet_data)

#use pprint to display data in proper format
pprint(sheet_data)