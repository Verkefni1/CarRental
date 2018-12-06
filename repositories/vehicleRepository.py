from models.Vehicle import Vehicle
import csv
import os

class VehicleRepository():

    def __init__(self, vehicle):
        self.__vehicle = []

    def add_vehicle(self, employee, manager, vehicle):
        with open("Vehicle.csv", "a+") as Vehicles_file:
            IDnumber = vehicle.get_IDnumber()
            body = vehicle.get_body()
            make = vehicle.get_make()
            model = vehicle.get_model()
            year = vehicle.get_year()
            color = vehicle.get_color()
            transmission = vehicle.get_transmission()
            Vehicles_file.write("{}, {}, {}, {}, {}, {}, {}\n".format(IDnumber, body, make, model, year, color, transmission))

    def get_vehicle(self, employee, vehicle):
        if self.__vehicle == []:
            with open("Vehicle.csv", "r") as Vehicle_file:
                for line in Vehicle_file.readlines():
                    IDnumber, body, make, model, year, color, transmission = line.split(",")
                    new_vehicle = Vehicle(IDnumber, body, make, model, year, color, transmission)
                    self.__vehicle.append(new_vehicle)
        return self.__vehicle

    def remove_vehicle(self, vehicle, IDnumber):
        with open("Vehicle.csv", 'r') as Vehicle_file:
            reader = csv.reader(Vehicle_file)
            with open("Vehicletmp.csv", 'w+') as Vehicle_file_tmp:
                writer = csv.writer(Vehicle_file_tmp)
                for row in reader:
                    if row[0] != IDnumber:
                        writer.writerow(row)
        os.rename('VehicleTmp.csv', 'Vehicle.csv')
    

