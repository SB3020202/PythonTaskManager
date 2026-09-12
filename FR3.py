""" ------------------------------------------- FR3 ------------------------------------------- """
class ElectricCar(Car):
    pass

class CombustionCar(Car):
    pass

e = ElectricCar("XX-11-YY", "Model 3", "Electric", "Available", date(2026, 5, 1))
print(e.plate)
