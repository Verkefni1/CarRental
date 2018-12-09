from models.Employee import Employee
from services.CarRentalServices import CarRentalServices
from services.EmployeeServices import EmployeeServices
from models.Vehicle import Vehicle
from ui.main_menu import MainMenu
import getpass

class vehicle_menu(object):
    def __init__(self, current_employee):
        self.current_employee = current_employee
    
    def home(self):

        # vehicle_menu needs to be in it's own class.
        # This UI file is getting really crowded.
        # by using self.method() where method is the name of the method we want to go to, we can go from menu to menu
        action = ""
        options = ["1", "2", "3", "4", "5"]
        print("=== Vehicle Menu ===\n")
        while action not in options:
            
            print("1. Display vehicles by availability\n2. Display Vehicle History\n3. Change Vehicle Status")
            if self.current_employee.is_manager():
                print("=== Management Options ===")
                print("4. Add Vehicle to Fleet\n5. Retire Vehicle")
            print("Press B to return to Main Menu")
            action = input("Enter: ").lower()

            if action == "1":
                # Display Vehicles by Availability
                # vehicle_menu.availability(current_employee)
                print("=== Displaying Vehicles by Availability ===")
                # main_menu.__car_rental_services.method()

            
            elif action == "2":
                # Display Vehicle History
                print("=== Display Vehicle History ===")
            
            elif action == "3":
                # Change Vehicle Status (Clean, Dirty, Out Of Order)
                print("=== Change Vehicle Status ===")
            
            elif action == "4":
                # Add Vehicle to Fleet
                if self.current_employee.is_manager():
                    print("=== Add Vehicle To Fleet ===")
                    IDnumber = input("Car ID: ")
                    body = input("Body: ")
                    make = input("Make: ")
                    model = input("Model: ")
                    year = input("Year: ")
                    color = input("Color: ")
                    transmission = input("Transmission: ")
                    print("")
                    new_vehicle = Vehicle(IDnumber, body, make, model, year, color, transmission)
                    self.__car_rental_service.add_vehicle(new_vehicle)#writes the vehicle into the vehicle.csv file
                else:
                    pass
                
            elif action == "5":
                # Retire Vehicle
                print("Get all reservations")

            elif action == "B".lower():
                print("Go back")
                MainMenu.home(self.current_employee)

            else:
                print("Invalid input")
