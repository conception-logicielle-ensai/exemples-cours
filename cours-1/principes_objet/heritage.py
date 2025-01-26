# Classe parente : Reservation
class Reservation:
    def __init__(self, name, date, price):
        self.name = name  # Nom de la personne qui réserve
        self.date = date  # Date de la réservation
        self.price = price  # Prix de la réservation

    def display_info(self):
        print(f"Réservation pour {self.name} à la date du {self.date}. Prix: {self.price}€")

    def confirm(self):
        print(f"La réservation pour {self.name} est confirmée.")

# Classe enfant : HotelReservation (hérite de Reservation)
class HotelReservation(Reservation):
    def __init__(self, name, date, price, num_nights):
        super().__init__(name, date, price)  # Appel au constructeur de la classe parente
        self.num_nights = num_nights  # Nombre de nuits réservées

    def display_info(self):
        super().display_info()  # Appel de la méthode de la classe parente
        print(f"Nombre de nuits: {self.num_nights}")

    def confirm(self):
        super().confirm()  # Appel de la méthode de la classe parente
        print(f"Réservation de l'hôtel pour {self.num_nights} nuit(s) confirmée.")

# Classe enfant : FlightReservation (hérite de Reservation)
class FlightReservation(Reservation):
    def __init__(self, name, date, price, flight_number):
        super().__init__(name, date, price)  # Appel au constructeur de la classe parente
        self.flight_number = flight_number  # Numéro de vol

    def display_info(self):
        super().display_info()  # Appel de la méthode de la classe parente
        print(f"Numéro de vol: {self.flight_number}")

    def confirm(self):
        super().confirm()  # Appel de la méthode de la classe parente
        print(f"Réservation du vol {self.flight_number} confirmée.")

# Utilisation des classes

# Création d'une réservation d'hôtel
hotel_reservation = HotelReservation("Alice", "2023-12-25", 200, 3)
hotel_reservation.display_info()
hotel_reservation.confirm()

# Création d'une réservation de vol
flight_reservation = FlightReservation("Bob", "2023-12-25", 150, "AF1234")
flight_reservation.display_info()
flight_reservation.confirm()