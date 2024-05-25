class Vehicle:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Mileage: {self.mileage} miles")

    def drive(self, miles):
        if miles > 0:
            self.mileage += miles
        else:
            print("Fals")

    def maintenance_needed(self):
        return self.mileage > 100.000

    def reset_mileage(self):
        self.mileage = 0

vehicle = Vehicle("Audi", "R8", 6800)
vehicle.display_info()
vehicle.drive(120)
vehicle.display_info()
print(vehicle.maintenance_needed())
vehicle.drive(6800)
print(vehicle.maintenance_needed())
vehicle.reset_mileage()
vehicle.display_info()
