from models.Employee import Employee

class Car_UI:
    def __init__(self):
        #self.__car_rental_service = CarRentalService()
        #self.__employee_services = EmployeeServices()
        self.name = "name" #Delete once we have the services

    def login(self):
        action = ""
        while action != "y":
            print("Print Login\n")
            username = input("Username: ").lower()
            password = input("Password: ")
            action = input("Submit?(Y/N): ").lower()
            
            if action == "y":
                Employee(username, password, True)#Might need to change this to false and make it so only the first person
                                                  #that enters in a UN and PW becomes admin 
                correct_inp = Employee().login(username, password)
                if correct_inp:
                    return correct_inp #Returns True if the input is correct
            else:
                print("Submit canceled\n")

    def main_menu(self):
        action = ""
        options = str([1, 2, 3, 4,])
        print("Welcome {}\n".format(Employee.get_username(self)))# Need to get the username here properly
        while action not in options:
            #print("Welcome {}\n".format(Car_UI.login)) ## Print the name each time he has to input?
            print("Here are your options:\n1. Car\n2. Customer\n3. Look up order \n4. Exit\n")
            action = input("Enter: ")

            if action == "1":
                print("Going to Car menu")
            elif action == "2":
                print("Going to Customer menu")
            elif action == "3":
                print("Going to Order menu")
            elif action == "4":
                print("Exiting program")
            else:
                print("Invalid input")

### MUST RUN ON NEW_FILE.PY OR ELSE IT WONT RUN
