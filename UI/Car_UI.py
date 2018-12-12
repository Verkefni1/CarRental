from models.Employee import Employee
from models.Vehicle import Vehicle
from models.Customer import Customer
from models.Reservation import Reservation
from services.CarRentalServices import CarRentalServices
from services.EmployeeServices import EmployeeServices
from serivces.ResServices import ResServices
import getpass

class Car_UI:
    def __init__(self):
        self.__car_rental_service = CarRentalServices()
        self.__employee_services = EmployeeServices()
        self.__res_services = ResServices()

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
                self.employee_menu(current_employee)

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

    def reservations_menu(self, current_employee):# Not sure how we are going to change from menu to menu.
        action = ""
        options = ["1", "2", "3", "4", "5"] 
        print("=== RESERVATIONS ===\n")
        while action not in options: # Need to use the orders file to check if the input matches an order number
            print("AVAILABLE OPTIONS:")
            print("1. Make reservation\n2. Lookup reservation\n3. Edit reservation\n4. Cancel reservation\n5. Go back")
            action = input("Enter: ")
            print("")

            if action == "1":#All this code for action 1 is just thinking how the process works. THIS IS NOT THE FINAL WORK
                customer_drivers_license = input("Drivers license number: ")
                body_type = input("Body type: ")
                from_date = input("From: ")
                to_date = input("To: ")

                if self.__res_services.check_dates(body_type, from_date, to_date):#Make this into a function in repo?
                    body_amount = self.__res_services.how_many(body_type)
                    print("There are {} {}'s available".format(body_amount, body_type))
                else:
                    print("No {} is available".format(body_type))
                insurance = input("Insurance?(Y/N): ").lower()
                if insurance == "y":#Make into a function in repo?
                    cost = self.__res_services.calc_res_cost(insurance)
                else:
                    cost = self.__res_services.calc_res_cost()
                CC = input("Enter Credit Card number: ")
                payment_method = input("Payment method (Cash/Credit): ").lower()#Maybe make this into a function in resServices and resRepo
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
                # New reservation
                # input customer details, create class with them, pass class into reservation services
                self.reservations_menu(current_employee)

            elif action == "2":
                #Search Reservations
                res_num = input("Enter reservation number: ")
                self.reservations_menu(current_employee)

            elif action == "3":
                res_num = input("Enter reservation number: ")
                self.reservations_menu(current_employee)
                # Don't need to tell user where computer is taking them
                # not like we have loading screens
                #print("Going back to main menu\n")

            elif action == "4":
                #cancel reservation
                res_num = input("Enter reservation number: ")
                self.reservations_menu(current_employee)

            elif action == "5":
                #Go back to main menu
                self.main_menu(current_employee)

            else:
                print("INPUT INVALID\n")
                self.reservations_menu(current_employee)

    def employee_menu(self, current_employee): # VIANEY IS WORKING ON THIS
        action = ""
        options = []
        print("=== EMPLOYEES ===\n")
        while action not in options:
            print("AVAILABLE OPTIONS:")
            print("1. Add employee\n2. Remove employee")
            action = input("Enter: ")
            print("")

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