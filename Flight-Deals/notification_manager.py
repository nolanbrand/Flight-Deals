import smtplib

MY_EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.text = ""

    def send_notification(self):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=self.text
            )

    def populate_text(self, dictionary):
        low_price = dictionary["price"]
        from_iata = dictionary["iata_departure"]
        to_city = dictionary["city_name"]
        to_iata = dictionary["iata_arrival"]
        depart_time = dictionary["departure_time"]
        arrive_time = dictionary["arrival_time"]

        self.text = (f"Subject:Lowest Price Flight to {to_city}\n\nOnly {low_price} Euros to fly from "
                     f"London-{from_iata} to {to_city}-{to_iata} with departure time of {depart_time} "
                     f"and arrival time of {arrive_time}.")
