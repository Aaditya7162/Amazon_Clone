class vehicle:
    def __init__(self,VehicleNumber,OwnerName,HoursParked):
        self.VehicleNumber=VehicleNumber
        self.OwnerName=OwnerName
        self.HoursParked=HoursParked
    def display_info(self):
        print(f"Vehicle Number: {self.VehicleNumber}")
        print(f"Owner Name: {self.OwnerName}")
        print(f"Number of Hours the vehicle is parked: {self.HoursParked}")
class car(vehicle):
    def charge(self):
        print(f"The charged value for car is ₹{self.HoursParked * 50}.")
class bike(vehicle):
    def charge(self):
        print(f"The charged value for bike is ₹{self.HoursParked*20}.")
class ev(vehicle):
    def charge(self):
        print(f"The charged value for ev is ₹{self.HoursParked*30}.")

car = car("HR26CA1234", "Aaditya", 4)
bike = bike("HR26BI5678", "Rahul", 4)
ev= ev("HR26EV9012", "Priya", 4)
print("----- CAR -----")
car.display_info()
car.charge()

print("\n----- BIKE -----")
bike.display_info()
bike.charge()

print("\n----- ELECTRIC VEHICLE -----")
ev.display_info()
ev.charge()