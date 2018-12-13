from models.Employee import Employee
from models.Vehicle import Vehicle
from models.Customer import Customer
from models.Reservation import Reservation
from services.CarRentalServices import CarRentalServices
from services.EmployeeServices import EmployeeServices
from services.ResServices import ResServices
import getpass

class Car_UI:
    def __init__(self):
        self.__car_rental_service = CarRentalServices()
        self.__employee_services = EmployeeServices()
        self.__res_services = ResServices()
        self.__current_employee = ""

    def ui_login(self):
        program_is_running = True
        print("====== Employee Login ======\n")
        username = input("Username: ").lower()
        print("-Password input is hidden-")
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

            while program_is_running == True:
                self.main_menu(current_employee)

        else:
            print("Invalid username or password\n")
            self.ui_login()

    def main_menu(self, current_employee): # DONE
        action = ""
        options = ["1", "2", "3", "4", "5"]
        print("Welcome {}\n".format(current_employee.get_username()))
        while action not in options:
            print("AVAILABLE OPTIONS:\n1. Vehicle Menu\n2. Customer Records\n3. Reservations \n4. Employee Options \n5. Exit\n")
            action = input("Enter: ")
            print("")

            if action == "1":
                print("=== Accessing Vehicle Menu ===\n")
                self.vehicle_menu(current_employee)

            elif action == "2":
                print("=== Accessing Customer Records ===\n")
                self.customer_menu(current_employee)

            elif action == "3":
                print("=== Accessing Reservations ===\n")
                self.reservations_menu(current_employee)

            elif action == "4":
                print("=== Accessing Employee Options ===\n")
                self.employee_menu()

            elif action == "5":
                print("=== Exiting Program ===")
                quit()

            else:
                print("Invalid input\n")

    def vehicle_menu(self, current_employee):
        # by using self.method() where method is the name of the method we want to go to, we can go from menu to menu        action = ""
        action = ""
        options = ["1", "2", "3", "4", "5", "6"]
        print("=== VEHICLES ===\n")
        while action not in options:
            print("AVAILABLE OPTIONS:") ## Print the name each time he has to input?
            #if current_employee == current_employee.is_manager():
            #    print("1. Display all available cars\n2. Display all rented cars\n3. Reserve a car\n4. Calculate rental costs\n5. Go back\n")
            #else:
            print("1. Add vehicle\n2. Search cars by body\n3. Display all available cars\n4. Display all reserved cars\n5. Retire vehicle\n6. Go back\n")
            action = input("Enter: ")
            print("")

            if action == "1": #DONE # THE VEHICLES FILE THAT CONTAINS ALL THE CARS MUST HAVE AN EMPTY
                print("Add vehicle")# LINE AT THE END OTHERWISE NEW VEHICLES WONT BE ADDED TO THE NEXT LINE
                IDnumber = input("Car ID: ")
                body = input("Body: ")
                make = input("Make: ")
                model = input("Model: ")
                year = input("Year: ")
                color = input("Color: ")
                transmission = input("Transmission: ")
                # Need attribute for wether or not the car is reserved or not. have it as a bool
                # when functions that display available and reserved cars we can just search each line
                # for reserved or available.
                print("")
                new_vehicle = Vehicle(IDnumber, body, make, model, year, color, transmission)
                self.__car_rental_service.add_vehicle(new_vehicle)#writes the vehicle into the vehicle.csv file
                self.vehicle_menu(current_employee)

            elif action == "2": # DONE
                options = ["sedan", "hatchback", "suv"]

                print("Search vehicle by Body\n")
                print("Body Types: Sedan, Hatchback, SUV\n")
                body_type = input("Body type: ").lower() # Which car body to search for
                print("")
                if body_type in options:
                    self.__car_rental_service.search_body_type(body_type) # prints each car of the type
                    print("")
                    self.vehicle_menu(current_employee)
                else:
                    print("No such body type available\n")
                    self.vehicle_menu(current_employee)

            elif action == "3": # DONE
                print("Get all available vehicles\n")
                self.__car_rental_service.get_all_vehicles()
                print("")
                self.vehicle_menu(current_employee)
                # Need to finish the repo for this action

            elif action == "4": # DONE
                print("Get all reservations\n")
                self.__car_rental_service.get_all_reserved()
                print("")
                self.vehicle_menu(current_employee)
                ## READ PLEASE ##
                # We could add another attribute to the vehicles class called is_reserved
                # as a boolean

            elif action == "5":# NOT DONE
                print("Retire vehicle\n")
                ID = input("Vehicle ID: ")
                self.__car_rental_service.retire_vehicle(ID)
                print("")

            elif action == "6": # DONE
                print("Go back")
                self.main_menu(current_employee)

            else:
                print("Invalid input")
                self.vehicle_menu(current_employee)

    def customer_menu(self, current_employee):
        # We need to implement these functions into the repo.
        # Both of these functiosn are required
        action = ""
        options = ["1", "2", "3", "4"]
        print("=== CUSTOMERS ===\n")
        while action not in options:
            print("AVAILABLE OPTIONS:")
            print("1. Register a customer\n2. Look up Customer\n3. Remove customer\n4. Go back\n")
            action = input("Enter: ")
            print("")

            if action == "1": ## DONE
                print("Registering a customer")
                first_name = input("First name: ")
                last_name = input("Last name: ")
                address = input("Address: ")
                drivers_license = input("Drivers license: ")
                SSN = input("SSN: ")
                new_customer = Customer(last_name, first_name, address, drivers_license, SSN)
                self.__car_rental_service.add_customer(new_customer)
                print("")
                self.customer_menu(current_employee)

            elif action == "2": ## NOT DONE
                print("Looking up customer")
                SSN = input("SSN: ")
                print("")
                self.__car_rental_service.search_customer(SSN)
                self.customer_menu(current_employee)

            elif action == "3": ## NOT DONE
                print("Remove customer")
                SSN = input("SSN: ")
                self.__car_rental_service.remove_customer(SSN)
                self.customer_menu(current_employee)

            elif action == "4":
                print("Going back to main menu")
                self.main_menu(current_employee)

            else:
                print("Invalid input")
                self.customer_menu(current_employee)

    def reservations_menu(self, current_employee):#THIS IS READY APPLY THIS TO YOUR UI MIGHT NEED TO CHANGE CURRENT_EMPLOYEE
        action = ""
        options = ["1", "2", "3", "4", "5"] 
        print("=== RESERVATIONS ===\n")
        while action not in options:
            print("AVAILABLE OPTIONS:")
            print("1. Make reservation\n2. Lookup reservation\n3. Edit reservation\n4. Cancel reservation\n5. Go back")
            action = input("Enter: ")
            print("")

            if action == "1":
                customer_drivers_license = input("Drivers license number: ")
                body_type = input("Body type: ")
                from_date = input("From: ")
                to_date = input("To: ")

                if self.__res_services.check_dates(body_type, from_date, to_date) > 0:
                    body_amount = self.__res_services.check_dates(body_type, from_date, to_date)
                    print("There are {} {}'s available for the dates selected".format(body_amount, body_type))
                else:
                    print("There are no {}'s available for the dates selected".format(body_type))
                insurance = input("Insurance?(Y/N): ").lower()
                if insurance == "y":
                    cost = self.__res_services.calc_res_cost(insurance)
                else:
                    cost = self.__res_services.calc_res_cost()
                CC = input("Enter Credit Card number: ")
                payment_method = input("Payment method (Cash/Credit): ").lower()
                if payment_method == "cash":
                    payment_method == "Cash"
                elif payment_method == "credit":
                    payment_method == "Credit"
                else:
                    print("Invalid input")
                    self.reservations_menu(current_employee)

                employee = current_employee
                res_num = self.__res_services.get_res_num()
                new_reservation = Reservation(res_num, customer_drivers_license, from_date, to_date, cost, CC, payment_method, employee)
                self.__res_services.make_res(new_reservation)
                print("")
                self.reservations_menu(current_employee)

            elif action == "2":
                #Search Reservations
                res_num = input("Enter reservation number: ")
                self.__res_services.search_res(res_num)
                self.reservations_menu(current_employee)

                #1,customer_license_num,CC_number,from_date,to_date,insurance(Y/N),body,employee

            elif action == "3":#Edit res
                edit_action = ""
                edit_options = ["1", "2", "3", "4", "5", "6", "7"]
                res_num = input("Enter reservation number: ")
                print("\nWhat would you like to change?\n")
                print("1. License number\n2. Credit Card\n3. From Date\n4. To Date\n5. Insurance\n6. Body\n7. Finish")#
                while edit_action not in edit_options:
                    edit_action = input("Enter: ")
                    if edit_action == "1":
                        change = input("Enter new info: ")
                        self.__res_services.edit_res(res_num, edit_action, change)
                    elif edit_action == "2":
                        change = input("Enter new info: ")
                        self.__res_services.edit_res(res_num, edit_action, change)
                    elif edit_action == "3":
                        change = input("Enter new info: ")
                        self.__res_services.edit_res(res_num, edit_action, change)
                    elif edit_action == "4":
                        change = input("Enter new info: ")
                        self.__res_services.edit_res(res_num, edit_action, change)
                    elif edit_action == "5":
                        change = input("Enter new info: ")
                        self.__res_services.edit_res(res_num, edit_action, change)
                    elif edit_action == "6":
                        change = input("Enter new info: ")
                        self.__res_services.edit_res(res_num, edit_action, change)
                    elif edit_action == "7":
                        self.reservations_menu(current_employee)
                    self.reservations_menu(current_employee)

            elif action == "4":
                #cancel reservation
                res_num = input("Enter reservation number: ")
                self.__res_services.cancel_res(res_num)
                self.reservations_menu(current_employee)

            elif action == "5":
                #Go back to main menu
                self.main_menu(current_employee)

            else:
                print("INPUT INVALID\n")
                self.reservations_menu(current_employee)

    def employee_menu(self):
        print("=== EMPLOYEE OPTIONS ===")
        print("1. Change Password\n7. Main Menu")
        print(self.__current_employee.is_manager())
        if self.__current_employee.is_manager():
            print("=== Management Only ===")
            print("2. Print Current Employees\n3. Grant Admin Rights\n4. View Employee Activity\n5. Add Employee\n6. Remove Employee")
        action = input()
        if action == "1":
            print("=== Change Password ===")
            print("Please Verify Current User")
            password = getpass.getpass()
            if self.__employee_services.login(self.__current_employee,password):
                print("Input Hidden - Enter New Password And Press Enter")
                new_password = getpass.getpass()
                self.__employee_services.employee_change_password(self.__current_employee.get_username(),new_password)
        
        elif action == "7":
            self.ui_menu()
        
        elif self.__current_employee.is_manager():
            if action == "2":
                if self.verify_pass():
                    print("Current Employees")
                    employee_list = self.__employee_services.get_all_employees()
                    self.print_list(employee_list)
                        
            elif action == "3":            
                if self.verify_pass():
                    print("Grant Admin Rights")
                    # new_admin musbt be string pulled from repo
                    new_admin = input("Enter Username: ")
                    confirm = input("Warning! You are about to give {} administration rights. Are you sure? (Y/N): ".format(new_admin)).lower()
                    if confirm == "y":
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
                        pass
                        #self.__employee_services.get_employee_history(employee_history)
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
        if self.__employee_services.login(self.__current_employee,password):
            return True
        else:
            print("Invalid Password")

    def not_employee(self):
        print("Employee Not Found")

    def print_list(self,passed_list):
        for item in passed_list:
            print(item)

    def calculate_costs(self,body,insurance,length):
        total_costs = self.__car_rental_service.calculate_costs(body,insurance,length)
        return total_costs

### MUST RUN ON NEW_FILE.PY OR ELSE IT WONT RUN