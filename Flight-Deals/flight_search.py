from amadeus import Client

FLIGHT_API_KEY = "Your_Amadeus_Flight_Key"
FLIGHT_API_SECRET = "Your_Amadeus_API_Secret"


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.amadeus = Client(
            client_id=FLIGHT_API_KEY,
            client_secret=FLIGHT_API_SECRET
        )
        self.origin_code = "LON"
        self.num_adults = 1

    def flight_get_request(self, destination_code=str, depart_date=str):
        flight_offers_response = self.amadeus.shopping.flight_offers_search.get(
            originLocationCode=self.origin_code,
            destinationLocationCode=destination_code,
            departureDate=depart_date,
            adults=self.num_adults
        )
        return flight_offers_response.data
