class Vehicle:
    def __init__(self, make, model, mileage):
        self.make = make
        self.model = model
        self.mileage = mileage

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Mileage: {self.mileage} miles")

    def drive(self, miles=0):
        self.mileage = miles
       miles = int(input("Введіть на скільки збільшився пробіг машини:"))
       result = self.mileage + miles
       print("Загальний пробіг:", result)

    def maintenance_needed(self):
       if self.mileage >= 100000:
           print(True)
       else:
           print(False)

    def reset_mileage(self):
        self.mileage = 0
        print("Пробіг дорівнює нулю")

vehicle = Vehicle("Audi", "R8", 0)
vehicle.display_info()
vehicle.drive()
vehicle..maintenance_needed()
vehicle.reset_mileage()
