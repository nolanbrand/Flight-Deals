import requests

GOOGLE_SHEETS_API = "https://api.sheety.co/eb9797a455434c4908c4c79bd8c8b1e7/flightDeals/prices"
GOOGLE_SHEETS_TOKEN = "Basic bmJyYW5kOk5lcmQxMjM0"
google_headers = {
    "Authorization": GOOGLE_SHEETS_TOKEN
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.get_response = {}

    def get_data(self):
        self.get_response = requests.get(url=GOOGLE_SHEETS_API, headers=google_headers)
        sheets_data = self.get_response.json()

        return sheets_data["prices"]
