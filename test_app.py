import unittest
from app import Driver, Passenger, Trip, RideSharingApp

class TestModels(unittest.TestCase):
    def test_driver_creation(self):
        driver = Driver(name="Carlos", car_model="Toyota Corolla")
        self.assertEqual(driver.name, "Carlos")
        self.assertEqual(driver.car_model, "Toyota Corolla")
        self.assertTrue(driver.is_available)
        self.assertIsNone(driver.current_trip)

    def test_passenger_creation(self):
        passenger = Passenger(name="Maria")
        self.assertEqual(passenger.name, "Maria")

    def test_trip_creation(self):
        passenger = Passenger(name="Maria")
        trip = Trip(passenger, "Origem", "Destino")
        self.assertEqual(trip.passenger, passenger)
        self.assertEqual(trip.origin, "Origem")
        self.assertEqual(trip.destination, "Destino")
        self.assertIsNone(trip.driver)
        self.assertEqual(trip.status, "requested")

    def test_trip_assign_driver(self):
        driver = Driver(name="Carlos", car_model="Toyota Corolla")
        passenger = Passenger(name="Maria")
        trip = Trip(passenger, "Origem", "Destino")
        trip.assign_driver(driver)
        self.assertEqual(trip.driver, driver)
        self.assertEqual(trip.status, "in_progress")
        self.assertFalse(driver.is_available)
        self.assertEqual(driver.current_trip, trip)

    def test_trip_complete(self):
        driver = Driver(name="Carlos", car_model="Toyota Corolla")
        passenger = Passenger(name="Maria")
        trip = Trip(passenger, "Origem", "Destino")
        trip.assign_driver(driver)
        trip.complete()
        self.assertEqual(trip.status, "completed")
        self.assertTrue(driver.is_available)
        self.assertIsNone(driver.current_trip)

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = RideSharingApp()
        self.driver1 = Driver(name="Carlos", car_model="Toyota Corolla")
        self.driver2 = Driver(name="Ana", car_model="Honda Civic")
        self.passenger1 = Passenger(name="Maria")

    def test_app_creation(self):
        self.assertEqual(len(self.app.drivers), 0)
        self.assertEqual(len(self.app.passengers), 0)
        self.assertEqual(len(self.app.trips), 0)

    def test_register_driver(self):
        self.app.register_driver(self.driver1)
        self.assertIn(self.driver1, self.app.drivers)

    def test_register_passenger(self):
        self.app.register_passenger(self.passenger1)
        self.assertIn(self.passenger1, self.app.passengers)

    def test_request_trip(self):
        self.app.register_driver(self.driver1)
        self.app.register_passenger(self.passenger1)
        trip = self.app.request_trip(self.passenger1, "Origem", "Destino")
        self.assertIn(trip, self.app.trips)
        self.assertEqual(trip.driver, self.driver1)
        self.assertEqual(trip.status, "in_progress")

    def test_request_trip_no_available_drivers(self):
        self.app.register_passenger(self.passenger1)
        trip = self.app.request_trip(self.passenger1, "Origem", "Destino")
        self.assertIn(trip, self.app.trips)
        self.assertIsNone(trip.driver)
        self.assertEqual(trip.status, "requested")

if __name__ == '__main__':
    unittest.main()
