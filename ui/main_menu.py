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
                self.__car_rental_service.remove_vehicle(vehicle_ID)

            elif action == "6":
                print("Go back")
                self.ui_menu()

            else:
                print("Invalid input")

    def customer_menu(self):# Not sure how we are going to change from menu to menu.
        print("=== CUSTOMERS ===\n")        
        action = ""
        options = ["1", "2", "3", "4", "5"]
        while action not in options:
            print("1. Register a customer\n"
            "2. Look Up Customer by name\n"
            "3. Look Up Customer by SSN\n"
            "4. Edit Customer"
            "5. Remove Custmer\n"
            "6. Main Menu\n")
            action = input("Enter: ")

            if action == "1":
                print("=== Registering New Customer ===")
                print("Enter Customer Details: ")
                last_name = input("Last Name: ")
                first_name = input("First Name: ")
                drivers_license = input("Driver's License Number: ")
                kennitala = input("Kennitala: ")
                address = input("Address: ")
                customer = Customer(last_name, first_name, drivers_license, kennitala, address)
                self.__car_rental_service.add_customer(self.__current_employee, customer)

            elif action == "2":
                print("=== Customer Search by Name ===")
                last_name = input("Last Name: ")
                first_name = input("First Name: ")
                self.__car_rental_service.search_customer_by_name(last_name, first_name)
            
            elif action == "3":
                print("=== Customer Search by SSN ===")
                kennitala = input("SSN: ")
                self.__car_rental_service.search_customer_by_ssn(ssn)

            elif action == "4":
                #Edit customer
                edit_action = ""
                edit_options = ["1", "2", "3", "4", "5", "6", "7"]
                ssn = input("Enter Customers SSN: ")
                
                print("\nWhat would you like to change?\n")
                
                print("1. First name\n"
                "2. Last name\n"
                "3. Address\n"
                "4. Drivers license\n"
                "5. SSN\n"
                "6. Current rental order number\n"
                "7. Finish") # Don't forget TRANSMISSION
                while edit_action not in edit_options:
                    edit_action = input("Enter: ")
                    if edit_action == "1":
                        change = input("Enter new info: ")
                        self.__car_rental_services.edit_customer(ssn, edit_action, change)
                    elif edit_action == "2":
                        change = input("Enter new info: ")
                        self.__car_rental_services.edit_customer(ssn, edit_action, change)                    
                    elif edit_action == "3":
                        change = input("Enter new info: ")
                        self.__car_rental_services.edit_customer(ssn, edit_action, change)
                    elif edit_action == "4":
                        change = input("Enter new info: ")
                        self.__car_rental_services.edit_customer(ssn, edit_action, change)
                    elif edit_action == "5":
                        change = input("Enter new info: ")
                        self.__car_rental_services.edit_customer(ssn, edit_action, change)
                    elif edit_action == "6":
                        change = input("Enter new info: ")
                        self.__car_rental_services.edit_customer(ssn, edit_action, change)
                    elif edit_action == "7":
                        self.customer_menu()
                    self.customer_menu()

            elif action == "5":
                if self.__current_employee.is_manager():
                    print("=== Remove Customer ===")
                    kennitala = input("SSN: ")
                    self.__car_rental_service.remove_customer(ssn)
                else:
                    pass

            elif action == "6":
                self.ui_menu()
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
                print("=== New Reservation ===")
                
                pass
            
            if action == "2":
                #Search Reservations
                print("=== Search Reservations ===")
                res_number = input("Input Reservation Number: ")
                self.__car_rental_service.get_reservation(res_number)
                userChoice = input("Press D for delete\n E for edit").upper()
                if userChoice == "e":
                    self.__car_rental_service.edit_reservation()
                


                #if red_number in ## need to use the orders file here
                
                # ALLOW TO DELETE RES HERE
            
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
            print("=== Change Password ===")
            print("Please Re-Enter Your Password")
            password = getpass.getpass()
            if self.__employee_services.login(self.__current_employee.get_username,password):
                print("Input Hidden - Enter New Password And Press Enter")
                new_password = getpass.getpass()
                self.__employee_services.employee_change_password(self.__current_employee,new_password)
        
        elif action == "7":
            self.ui_menu()
        
        elif self.__current_employee.is_manager():
            if action == "2":
                if self.verify_pass():
                    print("Current Employees")
                    for employee in self.__employee_services.get_all_employees():
                        print(employee)
                    
        
            elif action == "3":            
                if self.verify_pass():
                    print("Grant Admin Rights")
                    # new_admin musbt be string pulled from repo
                    new_admin = input("Enter Username: ")
                    confirm = input("Warning! You are about to give {} administration rights. Are you sure? (Y/N)").format(new_admin)
                    if confirm == "Y".lower():
                        if self.__employee_services.is_employee(new_admin):
                            self.__employee_services.make_admin(self.__current_employee,new_admin)
                        else:
                            self.not_employee()
                    elif confirm == "N".lower():
                        print("Operation Cancelled")
                    else:
                        print("Invalid Input")

            elif action == "4":
                if self.verify_pass():
                    print("View Employee History")
                    employee_history = input("Enter Username: ")
                    if self.__employee_services.is_employee(employee_history):
                    # must prompt for username and check for validity
                        self.__employee_services.get_employee_history(employee_history)
                    else:
                        self.not_employee()
            
            elif action == "5":
                if self.verify_pass():
                    print("Add Employee")
                    username = input("Username: ")
                    if not self.__employee_services.is_employee(username):
                        self.__employee_services.make_new_employee(self.__current_employee,username)
                    else:
                        print("Username Already Taken")

            elif action == "6":
                if self.verify_pass():
                    print("Remove Employee")
                    # variable to_remove is username of employee we're removing.
                    # Collected by user input and checked for validity before
                    # being passed into remove_employee method.
                    username = input("Username: ")
                    if self.__employee_services.is_employee(username):
                        self.__employee_services.remove_employee(self.__current_employee,username)
                    else:
                        self.not_employee()
        else:
            print("Invalid input")

    def verify_pass(self):
        print("Please Re-Enter Password")
        password = getpass.getpass()
        return self.__employee_services.login(self.__current_employee,password)

    def not_employee(self):
        print("Employee Not Found")

### MUST RUN ON NEW_FILE.PY OR ELSE IT WONT RUN