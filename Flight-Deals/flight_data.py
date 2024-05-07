class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, data, index):
        self.price = float(data[index]["price"]["grandTotal"])
        self.iata_departure = data[index]["itineraries"][0]["segments"][0]["departure"]["iataCode"]
        self.iata_arrival = data[index]["itineraries"][0]["segments"][-1]["arrival"]["iataCode"]
        self.time_departure = data[index]["itineraries"][0]["segments"][0]["departure"]["at"]
        self.time_arrival = data[index]["itineraries"][0]["segments"][-1]["arrival"]["at"]

