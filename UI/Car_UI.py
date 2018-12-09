from models.Employee import Employee
from services.CarRentalServices import CarRentalServices
from services.EmployeeServices import EmployeeServices
from models.Vehicle import Vehicle
import getpass

class Car_UI:
    def __init__(self):
        self.__car_rental_service = CarRentalServices()
        self.__employee_services = EmployeeServices()

    def ui_login(self):
        action = ""
        while action != "y":
            print("====== Employee Login ======\n")
            username = input("Username: ").lower()
            print("User password input is hidden. Press Enter to proceed.")
            password = getpass.getpass() # built-in Python module
            print("")
            # creates current_employee class using username and password
            # login() method checks if it's a valid employee and returns 
            # true if employee found in data file and given password matches. 
            # Next method checks for employee
            # admin status and sets it according to data file.
            current_employee = Employee(username, password)
            
            if self.__employee_services.login(current_employee,password):
                current_employee.manager = current_employee.is_manager()
                # Must pass current_employee class to main menu to 
                # carry employee data to method and rest of program
                self.main_menu(current_employee)
            elif action == "n":
                print("Invalid username or password")
                print("\n")

    def main_menu(self, current_employee):
        action = ""
        options = ["1", "2", "3", "4", "5"]
        print("=== 55 Car Rental ===")
        print("Welcome {}\n".format(current_employee.get_username()))
        while action not in options:
            print("Here are your options:\n1. Vehicle Menu\n2. Customer Records\n3. Reservations \n4. Employee Options \n5. Exit\n")
            action = input("What would you like to do?: ")
            print("\n")
            if action == "1":
                self.vehicle_menu(current_employee)
            elif action == "2":
                print("=== Accessing Customer Records ===\n")
                self.customer_menu(current_employee)
            elif action == "3":
                print("=== Accessing Reservations ===\n")
                self.reservations_menu(current_employee)
            elif action == "4":
                print("=== Accessing Employee Options ===\n")
                self.employee_menu(current_employee)
            elif action == "5":
                print("=== Exiting Program ===\n")
                quit()
            else:
                print("Invalid input\n")

    def vehicle_menu(self, current_employee):
        # by using self.method() where method is the name of the method we want to go to, we can go from menu to menu
        action = ""
        options = ["1", "2", "3", "4", "5"]
        print("=== Vehicle Menu ===\n")
        while action not in options:
            
            print("1. Display vehicles by availability\n2. Display Vehicle History\n3. Change Vehicle Status")
            if current_employee.is_manager():
                print("=== Management Options ===")
                print("4. Add Vehicle to Fleet\n5. Retire Vehicle")
            print("Press B to return to Main Menu")
            action = input("Enter: ").lower()

            if action == "1":
                # Display Vehicles by Availability
                print("=== Displaying Vehicles by Availability ===")
            
            elif action == "2":
                # Display Vehicle History
                
            
            elif action == "3":
                # Change Vehicle Status (Clean, Dirty, Out Of Order)
                print("Get Vehicle")
                ID = input("Car ID: ")
                print(self.__car_rental_service.get_vehicle(ID))#need help figuring this out


            elif action == "4":
                # Add Vehicle to Fleet
                if current_employee.is_manager():
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
                self.main_menu(current_employee)

            else:
                print("Invalid input")

    def customer_menu(self, current_employee):# Not sure how we are going to change from menu to menu.
        action = ""
        options = ["1", "2", "3"]
        print("Here are your customer options:")
        while action not in options:
            print("1. Register a customer\n2. Look up customer\n3. Go back\n")
            action = input("Enter: ")

            if action == "1":
                print("Registering a customer")
            elif action == "2":
                print("Looking up customer")
            elif action == "3":
                print("Going back to main menu")
                self.main_menu(current_employee)
            else:
                print("Invalid input")

    def reservations_menu(self, current_employee):# Not sure how we are going to change from menu to menu.
        action = ""
        options = ["1", "2", "3"] 
        print("=== RESERVATIONS ===")
        while action not in options: # Need to use the orders file to check if the input matches an order number
            print("AVAILABLE OPTIONS:")
            print("1. NEW RESERVATION\n2. SEARCH RESERVATIONS\n3. MAIN MENU")
            action = input()
            if action == "1":
                # New reservation
                # input customer details, create class with them, pass class into reservation services

            if action == "2":
                #Search Reservations
                order_num = input("ENTER RESERVATION NUMBER: ")
                #if order_num in ## need to use the orders file here
            elif action == "3":
                # Don't need to tell user where computer is taking them
                # not like we have loading screens
                #print("Going back to main menu\n")
                self.main_menu(current_employee)
            else:
                print("INPUT INVALID")
                
    def employee_menu(self, current_employee):
        action = ""
        options = []
        print("Here are your options:")
        print("1. Add employee\n2. Remove employee")

        if action == "1":
            print("Add employee")
        elif action == "2":
            print("Remove employee")
        elif action == "3":
            print("Make manager")
        elif action == "4":
            print("Get all employees")
        elif action == "5":
            print("Change password")
        elif action == "6":
            print("Go back")
            self.main_menu(current_employee)
        else:
            print("Invalid input")

### MUST RUN ON NEW_FILE.PY OR ELSE IT WONT RUN