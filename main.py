from app import RideSharingApp, Driver, Passenger

# 1. Inicializar a aplicação
app = RideSharingApp()

# 2. Registrar motoristas
driver1 = Driver(name="Carlos", car_model="Toyota Corolla")
driver2 = Driver(name="Ana", car_model="Honda Civic")
app.register_driver(driver1)
app.register_driver(driver2)

print("-" * 20)

# 3. Registrar passageiro
passenger1 = Passenger(name="Maria")
app.register_passenger(passenger1)

print("-" * 20)

# 4. Passageiro solicita uma viagem
trip1 = app.request_trip(passenger1, "Rua A, 123", "Avenida B, 456")

print("-" * 20)

# 5. Verificar o status da viagem e do motorista
print(f"Status da viagem: {trip1.status}")
print(f"Motorista da viagem: {trip1.driver.name}")
print(f"Disponibilidade do motorista {trip1.driver.name}: {trip1.driver.is_available}")

print("-" * 20)

# 6. Completar a viagem
trip1.complete()
print("Viagem completada.")
print(f"Status da viagem: {trip1.status}")
print(f"Disponibilidade do motorista {trip1.driver.name}: {trip1.driver.is_available}")

print("-" * 20)

# 7. Outro passageiro solicita uma viagem
passenger2 = Passenger(name="João")
app.register_passenger(passenger2)
trip2 = app.request_trip(passenger2, "Praça C, 789", "Rua D, 101")
