class Driver:
    def __init__(self, name, car_model):
        self.name = name
        self.car_model = car_model
        self.is_available = True
        self.current_trip = None

    def __str__(self):
        return f"{self.name} ({self.car_model})"

class Passenger:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Trip:
    def __init__(self, passenger, origin, destination):
        self.passenger = passenger
        self.origin = origin
        self.destination = destination
        self.driver = None
        self.status = "requested"

    def assign_driver(self, driver):
        self.driver = driver
        self.status = "in_progress"
        driver.is_available = False
        driver.current_trip = self

    def complete(self):
        self.status = "completed"
        if self.driver:
            self.driver.is_available = True
            self.driver.current_trip = None

class RideSharingApp:
    def __init__(self):
        self.drivers = []
        self.passengers = []
        self.trips = []

    def register_driver(self, driver):
        self.drivers.append(driver)
        print(f"Motorista {driver.name} registrado.")

    def register_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"Passageiro {passenger.name} registrado.")

    def request_trip(self, passenger, origin, destination):
        trip = Trip(passenger, origin, destination)
        self.trips.append(trip)
        print(f"Passageiro {passenger.name} solicitou uma viagem de {origin} para {destination}.")
        self.assign_trip(trip)
        return trip

    def find_available_driver(self):
        for driver in self.drivers:
            if driver.is_available:
                return driver
        return None

    def assign_trip(self, trip):
        available_driver = self.find_available_driver()
        if available_driver:
            trip.assign_driver(available_driver)
            print(f"Motorista {available_driver.name} foi atribuído à viagem de {trip.passenger.name}.")
        else:
            print("Nenhum motorista disponível no momento.")
