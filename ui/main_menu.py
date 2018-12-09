from models.Employee import Employee
from models.Vehicle import Vehicle
from models.customer import Customer

from services.CarRentalServices import CarRentalServices
from services.EmployeeServices import EmployeeServices

import getpass

class MainMenu:
    def __init__(self):
        self.__car_rental_service = CarRentalServices()
        self.__employee_services = EmployeeServices()
        self.__current_employee = ""
        
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
                self.__current_employee = current_employee
                # self.__current_employee.manager = current_employee.is_manager()
                # Must pass current_employee class to main menu to 
                # carry employee data to method and rest of program
                self.ui_menu()
            else:
                print("Invalid username or password")
                print("\n")

    def ui_menu(self):
        action = ""
        options = ["1", "2", "3", "4", "5", "6"]
        print("=== 55 Car Rental - Main Menu ===")
        print("Welcome {}\n".format(self.__current_employee.get_username()))
        while action not in options:
            print("1. Vehicle Menu\n2. Customer Records\n3. Reservations \n4. Employee Options \n5. Log Out \n6. Exit\n")
            action = input("What would you like to do?: ")
            print("\n")
            if action == "1":
                self.vehicle_menu()
            elif action == "2":
                self.customer_menu()
            elif action == "3":
                self.reservations_menu()
            elif action == "4":
                self.employee_menu()
            elif action == "5":
                print("=== Logging Out ===\n")
                self.ui_login()
            elif action == "6":
                quit()
            else:
                print("Invalid input\n")

    def vehicle_menu(self):
        action = ""
        options = ["1", "2", "3", "4", "5"]
        print("=== VEHICLES ===\n")
        while action not in options:
            
            print("1. Display vehicles by availability\n2. Display Vehicle History\n3. Change Vehicle Status")
            if self.__current_employee.is_manager():
                print("=== Management Options ===")
                print("4. Add Vehicle to Fleet\n5. Retire Vehicle")
            print("6. Main Menu")
            
            action = input("Enter: ").lower()

            if action == "1":
                # Display Vehicles by Availability
                print("=== Displaying Vehicles by Availability ===")
                self.__car_rental_service.get_vehicles_by_availability(self.__current_employee)
            
            elif action == "2":
                # Display Vehicle History
                print("=== Display Vehicle History ===")
                vehicle_ID = input("Enter Vehicle ID: ")
                self.__car_rental_service.get_vehicle_history(self.__current_employee,vehicle_ID)
            
            elif action == "3":
                # Change Vehicle Status (Clean, Dirty, Out Of Order)
                print("=== Change Vehicle Status ===")
                vehicle_ID = input("Enter Vehicle ID: ")
                self.__car_rental_service.change_vehicle_status(self.__current_employee,vehicle_ID)

            
            elif action == "4":
                # Add Vehicle to Fleet
                if self.__current_employee.is_manager():
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
                print("=== Retire Vehicle ===")
                vehicle_ID = input("Enter Vehicle ID: ")
                self.__car_rental_service.remove_vehicle(vehicle)

            elif action == "6":
                print("Go back")
                self.ui_menu()

            else:
                print("Invalid input")

    def customer_menu(self):# Not sure how we are going to change from menu to menu.
        print("=== CUSTOMERS ===\n")        
        action = ""
        options = ["1", "2", "3"]
        while action not in options:
            print("1. Register a customer\n2. Look up customer\n3. Main Menu\n")
            action = input("Enter: ")

            if action == "1":
                print("=== Registering New Customer ===")
                print("Enter Customer Details: ")
                last_name = input("Last Name: ")
                first_name = input("First Name: ")
                drivers_id = input("Driver's License Number: ")
                kennitala = input("Kennitala: ")
                address = input("Address: ")
                customer = Customer(customer)
                self.__car_rental_service.add_customer(customer)

            elif action == "2":
                print("=== Customer Search ===")
                last_name = input("Last Name: ")
                first_name = input("First Name: ")
                self.__car_rental_service.search_customer(last_name,first_name)
            
            elif action == "3":
                self.ui_menu(current_employee)
            else:
                print("Invalid input")

    def reservations_menu(self):# Not sure how we are going to change from menu to menu.
        action = ""
        options = ["1", "2", "3","4"] 
        print("=== RESERVATIONS ===")
        while action not in options: # Need to use the orders file to check if the input matches an order number
            print("1. New Reservation\n2. Search Reservations\n3. Display All Reservations\n4. Main Menu")
            action = input()
            if action == "1":
                # New reservation
                # input customer details, create class with them, pass class into reservation services
                print("New Reservation")
                pass
            
            if action == "2":
                #Search Reservations
                print("Search Reservations")
                #order_num = input("Input Reservation Number: ")
                #if order_num in ## need to use the orders file here
                """ self.__car_rental_service.get_reservation() """
            elif action == "3":
                ## Show all reservations
                print("Showing All Reservations")
                self.__car_rental_service.get_all_reservations(self.__current_employee)

            elif action == "4":
                # Return to Main Menu
                self.ui_menu()
            else:
                print("INPUT INVALID")
                
    def employee_menu(self):
        print("=== EMPLOYEE OPTIONS ===")
        print("1. Change Password\n6. Main Menu")
        if self.__current_employee.is_manager():
            print("=== Management Only ===")
            print("2. Print Current Employees\n3. Grant Admin Rights\n4. View Employee Activity\n5. Add Employee\n6. Remove Employee")
        action = input()
        if action == "1":
            print("Change Password")
            self.__car_rental_service(self.__current_employee)
        
        elif action == "7":
            self.ui_menu()
        
        elif self.__current_employee.is_manager():
            if action == "2":
                print("Print Current Employees")
                self.__car_rental_service.get_all_employees(self.__current_employee)
        
            elif action == "3":            
                print("Grant Admin Rights")
                # new_admin musbt be string pulled from repo
                self.__car_rental_service.make_admin(self.__current_employee,new_admin)
            elif action == "4":
                print("View Employee History")
                # must prompt for username and check for validity
                self.__car_rental_service.get_employee_history(employee_username)
            
            elif action == "5":
                print("Add Employee")
                # Collect new employee info, pass to Employee() class, feed into
                # method in Services
                self.__car_rental_service.make_new_employee()
            elif action == "6":
                print("Remove Employee")
                # variable to_remove is username of employee we're removing.
                # Collected by user input and checked for validity before
                # being passed into remove_employee method.
                self.__car_rental_service.remove_employee(self.__current_employee,to_remove)
        else:
            print("Invalid input")

### MUST RUN ON NEW_FILE.PY OR ELSE IT WONT RUN