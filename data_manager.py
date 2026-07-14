import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT= "SHEETY ENDPOINT"

class DataManager:

    def __init__(self):
        self.user=os.environ["SHEETY_USERNAME"]
        self.password=os.environ["SHEETY_PASSWORD"]
        self.authorization=HTTPBasicAuth(self.user,self.password)
        self.destination_data={}

    def get_destination_data(self):
        #use sheety api to get all data in sheet and print it out
        response=requests.get(url=SHEETY_PRICES_ENDPOINT,auth=self.authorization)
        data=response.json()
        self.destination_data=data["prices"]
        return self.destination_data #print data
