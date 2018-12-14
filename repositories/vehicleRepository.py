from models.Vehicle import Vehicle
import csv
import os

class VehicleRepository(object):

    def __init__(self):
        self.__vehicle_list = []

    def add_vehicle(self, vehicle):
        """
        Takes in a vehicle class and
        writes it into the appropriate
        CSV file
        """
        with open("Vehicle.csv", "a+") as Vehicles_file:
            IDnumber = vehicle.get_IDnumber()
            body = vehicle.get_body()
            make = vehicle.get_make()
            model = vehicle.get_model()
            year = vehicle.get_year()
            color = vehicle.get_color()
            transmission = vehicle.get_transmission()
            Vehicles_file.write("{}, {}, {}, {}, {}, {}, {}\n").format(IDnumber, body, make, model, year, color, transmission)

    def get_all_vehicles(self):
        """
        Returns list of lists with all vehicle 
        information in vehicle data file
        """
        if self.__vehicle_list == []:
            with open("./data/vehicle.csv", "r") as Vehicle_file:
                reader = csv.reader(Vehicle_file)
                for line in reader:
                    self.__vehicle_list.append(line)

        return self.__vehicle_list

    def remove_vehicle(self, IDnumber):
        """
        Compares parameter vehicle IDnumber to those in vehicle data file
        and removes vehicle with IDnumber match, of which there should
        only be one.
        """
        with open("./data/vehicle.csv", 'r') as Vehicle_file:
            reader = csv.reader(Vehicle_file)
            with open("./data/Vehicletmp.csv", 'w+') as Vehicle_file_tmp:
                writer = csv.writer(Vehicle_file_tmp)
                for row in reader:
                    if row[0] != IDnumber:
                        writer.writerow(row)
        os.remove('./data/vehicle.csv')
        os.rename('./data/VehicleTmp.csv', './data/vehicle.csv')
