from models.Employee import Employee
from services.CarRentalServices import CarRentalServices
from services.EmployeeServices import EmployeeServices

class Car_UI:
    def __init__(self):
        self.__car_rental_service = CarRentalServices()
        self.__employee_services = EmployeeServices()
        


    def ui_login(self):
        action = ""
        while action != "y":
            print("====== Employee Login ======\n")
            username = input("Username: ").lower()
            password = input("Password: ")
            
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
            else:
                print("Invalid username or password.\n")

    def main_menu(self,current_employee):
        action = ""
        options = str([1, 2, 3, 4, 5,])
        print("Welcome {}\n".format(current_employee.get_username()))
        while action not in options:
            
            print("Here are your options:\n1. Vehicle Menu\n2. Customer Records\n3. Reservations \n4. Employee Options \n5. Exit\n")
            action = input("Enter option number: ")

            if action == "1":
                print("=== Accessing Vehicle Menu ===")
                self.vehicle_menu(current_employee)
            elif action == "2":
                print("=== Accessing Customer Records ===")
                self.customer_menu(current_employee)
            elif action == "3":
                print("=== Accessing Reservations ===")
                self.reservations_menu(current_employee)
            elif action == "4":
                print("=== Accessing Employee Options ===")
                self.employee_menu(current_employee)
            elif action == "5":
                print("=== Exiting Program ===")
                quit()
            else:
                print("Invalid input")
    
    def vehicle_menu(self,current_employee):
        pass
    
    def customer_menu(self,current_employee):
        pass
    
    def reservations_menu(self,current_employee):
        pass
    
    def employee_menu(self,current_employee):
        pass
### MUST RUN ON NEW_FILE.PY OR ELSE IT WONT RUN
