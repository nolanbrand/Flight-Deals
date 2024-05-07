import requests

GOOGLE_SHEETS_API = "Your_Google_Sheet"
GOOGLE_SHEETS_TOKEN = "Your_Google_Sheet_Token"
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
