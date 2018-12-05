

class VehicleRepository():

    def __init__(self, vehicle):
        self.vehicle = []

    def add_vehicle(self, employee, manager, vehicle):
        with open("Vehicle.csv", "a+") as Vehicles_file:
            IDnumber = Vehicle.get_IDnumber()
            body = Vehicle.get_body()
            make = Vehicle.get_make()
            model = Vehicle.get_model()
            year = Vehicle.get_year()
            color = Vehicle.get_color()
            transmission = Vehicle.get_transmission()

    def get_vehicle(self, employee, vehicle):
        if self.vehicle == []
        with open("Vehicle.csv", "r") as Vehicle_file
            for line in Vehicle_file.readlines():
                IDnumber, body, make, model, year, color, transmission = line.split(",")
                new_vehicle = Vehicle(IDnumber, body, make, model, year, color, transmission)
                self.vehicle.append(new_vehicle)
        return self.vehicle

    def remove_vehicle(self, vehicle):
        pass
    

