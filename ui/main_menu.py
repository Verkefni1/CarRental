from models.Employee import Employee
from models.Vehicle import Vehicle
from models.Customer import Customer
from models.Reservation import Reservation

from services.CarRentalServices import CarRentalServices
from services.EmployeeServices import EmployeeServices
from services.ResServices import ResServices

import getpass


class MainMenu:
    def __init__(self):
        self.__car_rental_service = CarRentalServices()
        self.__employee_services = EmployeeServices()
        self.__res_services = ResServices()
        self.__current_employee = ""

    def ui_login(self):
        action = ""
        while action != "y":
            print("Employee Login")
            username = input("Username: ").lower()
            print("User password input is hidden. Press Enter to proceed.")
            password = getpass.getpass()
            if self.__employee_services.get_employee_class(username, password):
                self.__current_employee = (self.__employee_services.
                                           get_employee_class(username,
                                                              password))
                print(self.__current_employee)
                self.ui_menu()
            else:
                print("Invalid Username Or Password\n")

    def ui_menu(self):
        action = ""
        options = ["1", "2", "3", "4", "5", "6"]
        self.header_1("55 Car Rental - Main Menu")

        self.header_1("Welcome {}".format(
                       self.__current_employee.get_username()))
        print("**********************")
        self.header_2("Todays's Rates: ")
        self.display_rates()
        print("**********************\n")
        
        while action not in options:
            print("1. Vehicle Menu\n"
                  "2. Customer Records\n"
                  "3. Reservations\n"
                  "4. Employee Options\n"
                  "5. Log Out\n"
                  "6. Exit\n")
            action = input("What would you like to do?: ")
            print("")
            if action == "1":
                self.vehicle_menu()
            elif action == "2":
                self.customer_menu()
            elif action == "3":
                self.reservations_menu()
            elif action == "4":
                self.employee_menu()
            elif action == "5":
                print("Logging Out {}...".format(self.__current_employee.
                                                 get_username()))
                self.ui_login()
            elif action == "6":
                quit()
            else:
                print("Invalid input\n")

    def vehicle_menu(self):
        action = ""
        options = ["1", "2", "3", "4", "5"]
        self.header_1("Vehicles")
        while action not in options:

            print("1. Display Available Vehicles\n"
                  "2. Display Currently Rented Vehicles")
            if self.__current_employee.is_manager():
                self.format_warning("Management Options")
                print("3. Add Vehicle to Fleet\n"
                      "4. Retire Vehicle\n")
            print("5. Main Menu")

            action = input("Enter: ").lower()

            if action == "1":
                print("Displaying Available Vehicles")
                available_list = self.__res_services.display_available_vehicles()
                self.format_list_of_list(available_list)
            elif action == "2":
                print("Displaying Rented Vehicles")
                reserved_today = self.__res_services.display_reserved_vehicles()
                self.print_list(reserved_today)

            elif action == "3":
                if self.__current_employee.is_manager():
                    print("Add Vehicle To Fleet")
                    IDnumber = input("Car ID: ")
                    body = input("Body: ")
                    make = input("Make: ")
                    model = input("Model: ")
                    year = input("Year: ")
                    color = input("Color: ")
                    transmission = input("Transmission: ")
                    print("")
                    new_vehicle = Vehicle(IDnumber, body, make, model,
                                          year, color, transmission)
                    self.__car_rental_service.add_vehicle(new_vehicle)
                else:
                    pass

            elif action == "4":
                # Retire Vehicle
                print("=== Retire Vehicle ===")
                vehicle_ID = input("Enter Vehicle ID: ")
                self.__car_rental_service.remove_vehicle(vehicle_ID)

            elif action == "5":
                print("Go back")
                self.ui_menu()

            else:
                print("Invalid input")

    def customer_menu(self):
        print("=== CUSTOMERS ===\n")
        action = ""
        options = ["1", "2", "3", "4", "5", "6"]
        while action not in options:
            print("1. Register a customer\n"
                  "2. Look Up Customer\n"
                  "3. Edit A customer\n"
                  "4. Remove A Customer\n"
                  "5. Display customers\n"
                  "6. Main menu")
            print()
            action = input("Enter: ")
            print()

            if action == "1":
                print("=== Registering New Customer ===")
                print("Enter Customer Details: ")
                last_name = input("Last Name: ")
                first_name = input("First Name: ")
                address = input("Address: ")
                ssn = input("SSN: ")
                drivers_license = input("Driver's License Number: ")
                customer = Customer(last_name, first_name, address, ssn,
                                    drivers_license)
                self.__car_rental_service.add_customer(
                    self.__current_employee, customer)
                self.customer_menu()

            elif action == "2":
                print("=== Customer Search ===")
                ssn = input("Enter Customers SSN: ")
                customer_info = self.__car_rental_service.search_customer_by_ssn(ssn)
                print(customer_info)
                print()
                self.customer_menu()

            elif action == "3":  # Edit customer
                edit_action = ""
                edit_options = ["1", "2", "3", "4", "5", "6", "7"]

                ssn = input("Enter Customers SSN: ")

                print("\nWhat would you like to change?\n")

                print("1. First name\n"
                      "2. Last name\n"
                      "3. Address\n"
                      "4. Drivers license\n"
                      "5. Current rental order number\n"
                      "7. Finish\n")
                while edit_action not in edit_options:
                    edit_action = input("Enter: ")
                    if edit_action == "1":
                        change = input("Enter new info: ")
                        self.__car_rental_service.edit_customer(
                            ssn, edit_action, change)
                    elif edit_action == "2":
                        change = input("Enter new info: ")
                        self.__car_rental_service.edit_customer(
                            ssn, edit_action, change)
                    elif edit_action == "3":
                        change = input("Enter new info: ")
                        self.__car_rental_service.edit_customer(
                            ssn, edit_action, change)
                    elif edit_action == "4":
                        change = input("Enter new info: ")
                        self.__car_rental_service.edit_customer(
                            ssn, edit_action, change)
                    elif edit_action == "5":
                        change = input("Enter new info: ")
                        self.__car_rental_service.edit_customer(
                            ssn, edit_action, change)
                    elif edit_action == "6":
                        self.customer_menu()
                    self.customer_menu()

            elif action == "4":
                if self.__current_employee.is_manager():
                    print("=== Remove A Customer ===")
                    ssn = input("Enter Customers SSN: ")
                    self.__car_rental_service.remove_customer(ssn)
                    self.customer_menu()
                else:
                    pass

            elif action == "5":
                self.header_2("Displaying All Customers")
                all_cust = self.__car_rental_service.get_all_customers()
                self.print_list(all_cust)
                print()
                self.customer_menu()

            elif action == "6":
                self.ui_menu()
            else:
                print("Invalid input")

    def reservations_menu(self):
        action = ""
        options = ["1", "2", "3", "4", "5"]
        self.header_1("Reservations")
        while action not in options:
            print("AVAILABLE OPTIONS:")
            print("1. Make reservation\n"
                  "2. Lookup reservation\n"
                  "3. Edit reservation\n"
                  "4. Cancel reservation\n"
                  "5. Go back")
            action = input("Enter: ")
            print("")

            if action == "1":
                self.header_2("Making a Reservation")
                customer_drivers_license = input("Drivers license number: ")
                body_type = input("Body type: ")
                print("Enter dates in this format (yyyy/mm/dd)")
                start_date = input("From: ")
                end_date = input("To: ")

                body_amount = self.__res_services.check_availability(
                                     body_type, start_date, end_date)
                if body_amount > 0:
                    print("There are {} {}'s available for the dates selected".
                          format(body_amount, body_type))
                else:
                    print("There are no {}'s available for the dates selected".
                          format(body_type))

                insurance = input("Insurance?(Y/N): ").lower()
                if insurance == "y":
                    insurance = True
                elif insurance == "n":
                    insurance = False
                else:
                    print("Invalid input")
                    self.reservations_menu()

                res_length = self.__res_services.get_res_length(
                                           start_date, end_date)
                ##  YOU ARE HERE
                cost = self.__res_services.calculate_costs(
                          body_type, insurance, res_length)
                # COST NEEDS TO BE PUT SOMEWHERE WHERE WE CAN PRINT IT OUT

                credit_card = input("Enter Credit Card number: ")
                payment_method = input("Payment method "
                                       "(Enter Cash or Credit): ").lower()
                if payment_method != "cash" and payment_method != "credit":
                    print("Invalid input")
                    self.reservations_menu()

                reservation_number = (self.__res_services.
                                      make_reservation_number())

                new_reservation = Reservation(reservation_number,
                                              customer_drivers_license,
                                              credit_card, start_date,
                                              end_date, insurance,
                                              payment_method, body_type,
                                              (self.__current_employee.
                                               get_username()))
                self.__res_services.make_res(new_reservation)
                print("")
                self.reservations_menu()

            elif action == "2":
                # Search Reservations
                res_num = input("Enter reservation number: ")
                search_results = (self.__res_services.search_res(res_num))
                print(search_results)
                self.reservations_menu()

            elif action == "3":
                # Edit res
                self.header_2("Edit Reservation")
                edit_action = ""
                edit_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
                res_num = input("Enter Reservation Number: ")
                search_results = (self.__res_services.search_res(res_num))
                print(search_results)
                if search_results == "Reservation Not Found":
                    self.reservations_menu()
                print("\nWhat would you like to change?\n")

                print("1. License number\n"
                      "2. Credit Card\n"
                      "3. From Date\n"
                      "4. To Date\n"
                      "5. Insurance\n"
                      "6. Body\n"
                      "7. Transmission\n"
                      "8. Vehicle ID\n"
                      "9. Return or Release Keys\n"
                      "10. Finish")
                while edit_action not in edit_options:
                    edit_action = input("Enter: ")
                    if edit_action == "1":
                        change = input("Enter New License Number: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "2":
                        change = input("Enter New CC Number: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "3":
                        change = input("New Start Date: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "4":
                        change = input("New End Date: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "5":
                        change = input("Insurance: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "6":
                        change = input("Enter New Payment Method: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "7":
                        change = input("Enter New Body Type: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "8":
                        change = input("Enter New Vehicle ID: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                    elif edit_action == "9":
                        change = input("Keys In / Keys Out: ")
                        self.__res_services.edit_res(res_num, edit_action,
                                                     change)
                        reservation = (self.__res_services.search_res(res_num))
                        print(reservation)
                    elif edit_action == "10":
                        self.reservations_menu()

            elif action == "4":
                # cancel reservation
                self.header_2("Cancel Reservation")
                res_num = input("Enter reservation number: ")
                search_results = (self.__res_services.search_res(res_num))
                print(search_results)

                if search_results == "Reservation Not Found":
                    self.reservations_menu()
                confirm = (input("Warning! Are you sure you want "
                                 "to cancel reservation number {}? "
                                 "This cannot be undone. (Y/N)".format(
                                  res_num)))
                if confirm == "Y".lower():
                    self.__res_services.cancel_res(res_num)
                    print("Reservation Number: {}"
                          "has been cancelled.".format(res_num))
                else:
                    print("Operation Cancelled")
                self.reservations_menu()

            elif action == "5":
                # Go back to main menu
                self.ui_menu()

            else:
                print("INPUT INVALID\n")
                self.reservations_menu()

    def employee_menu(self):
        self.header_1("employee options")
        print("1. Change Password\n"
              "6. Main Menu\n")

        if self.__current_employee.is_manager():
            self.header_1("Management Only")
            print("2. Print Current Employees\n"
                  "3. Grant Admin Rights\n"
                  "4. Add Employee\n"
                  "5. Remove Employee")
        action = input()
        if action == "1":
            self.header_1("Change Password")
            self.format_warning("Please Verify Current User")
            password = getpass.getpass()
            if self.__employee_services.login(self.__current_employee,
                                              password):
                print("Input Hidden - Enter New Password And Press Enter")
                new_password = getpass.getpass()
                self.__employee_services.employee_change_password(
                    self.__current_employee.get_username(), new_password)

        elif action == "6":
            self.ui_menu()

        elif self.__current_employee.is_manager():
            if action == "2":
                if self.verify_pass():
                    print("Current Employees")
                    employee_list = (self.__employee_services.
                                     get_all_employees())
                    self.print_list(employee_list)

            elif action == "3":
                if self.verify_pass():
                    print("Grant Admin Rights")
                    # new_admin musbt be string pulled from repo
                    new_admin = input("Enter Username: ")
                    self.format_warning("Warning !!! ")
                    confirm = (input("You are about to give {} "
                                     "administration rights. "
                                     "Are you sure? (Y/N): ".
                                     format(new_admin)).lower())
                    if confirm == "y":
                        if self.__employee_services.is_employee(new_admin):
                            self.__employee_services.make_admin(
                                self.__current_employee, new_admin)
                            self.header_2("{} is now admin".format(new_admin))
                            self.employee_menu()
                        else:
                            self.not_employee()
                    elif confirm == "N".lower():
                        print("Operation Cancelled")
                        self.employee_menu()
                    else:
                        print("Invalid Input")
                        self.employee_menu()

            elif action == "4":
                if self.verify_pass():
                    print("Add Employee")
                    username = input("Username: ")
                    if not self.__employee_services.is_employee(username):
                        self.__employee_services.make_new_employee(
                                 self.__current_employee, username)
                    else:
                        print("Username Already Taken")

            elif action == "5":
                if self.verify_pass():
                    print("Remove Employee")
                    username = input("Username: ")
                    if self.__employee_services.is_employee(username):
                        self.__employee_services.remove_employee(
                               self.__current_employee, username)
                    else:
                        self.not_employee()

        else:
            print("Invalid input")

    def verify_pass(self):
        print("Please Re-Enter Password")
        password = getpass.getpass()
        if self.__employee_services.login(self.__current_employee, password):
            return True
        else:
            print("Invalid Password")

    def not_employee(self):
        print("Employee Not Found")

    def print_list(self, passed_list):
        for item in passed_list:
            print(item)

    def header_1(self, header_text):
        """
        Highest emphasis headers
        === HEADER 1 ===

        """
        header_text = header_text.upper()
        print("\n=== {} ===".format(header_text))

    def header_2(self, header_text):
        """
        -- Header 2 --
        """
        header_text = header_text.capitalize()
        print("\n--- {} ---".format(header_text))
    
    def format_warning(self, warning_text):
        """
        ****** WARNING ******
        """
        warning_text = warning_text.upper()
        print("\n***** {} *****".format(warning_text))

    def format_list_of_list(self, the_list):
        
        print("{} {}s\n"
              "{} {}s\n"
              "{} {}s\n".format(the_list[0], the_list[1], the_list[2],
                                the_list[3], the_list[4], the_list[5]))

    def display_rates(self):
        rate_list = self.__res_services.get_rates_list()
        for rate in rate_list[0:-1]:
            print("{}: ${:.2f}".format(rate[0].capitalize(), float(rate[1])))
