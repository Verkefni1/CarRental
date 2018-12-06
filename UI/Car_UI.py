from models.Employee import Employee

class Car_UI:
    def __init__(self):
        #self.__car_rental_service = CarRentalService()
        #self.__employee_services = EmployeeServices()
        self.name = "name" #Delete once we have the services

    def login(self):
        action = ""
        while action != "y":
            print("Please Login\n")
            username = input("Username: ").lower()
            password = input("Password: ")
            action = input("Submit?(Y/N): ").lower()
            print("\n")

            if action == "y":
                Employee(username, password, True)#Might need to change this to false and make it so only the first person
                                                  #that enters in a UN and PW becomes admin 
                correct_inp = Employee().login(username, password)
                if correct_inp:
                    self.main_menu()
                    #current_user = username
                    #return correct_inp, current_user #Returns True if the input is correct
            elif action == "n":
                print("Submit canceled\n")

    def main_menu(self):
        action = ""
        options = ["1", "2", "3", "4"]
        print("Welcome {}\n".format("Jon"))# Need to get the username here properly
        while action not in options:
            #print("Welcome {}\n".format(Car_UI.login)) ## Print the name each time he has to input?
            print("Here are your options:\n1. Car\n2. Customer\n3. Look up order \n4. Exit\n")
            action = input("Enter: ")

            if action == "1":
                print("Going to Car menu\n")
                self.car_menu()
            elif action == "2":
                print("Going to Customer menu")
                self.customer_menu()
            elif action == "3":
                print("Going to Order menu")
                self.order_menu()
            elif action == "4":
                print("\nExiting program")
                exit
            else:
                print("Invalid input")

    def car_menu(self):# by using self.method() where method is the name of the method we want to go to, we can go from menu to menu
        action = ""
        options = ["1", "2", "3", "4", "5"]
        while action not in options:
            print("Here are your car options:") ## Print the name each time he has to input?
            print("1. Display all available cars\n2. Display rented cars\n3. Reserve a car\n4. Calculate rental costs\n5. Go back\n")
            action = input("Enter: ")

            if action == "1":
                print("Display all available cars")
            elif action == "2":
                print("Display all rented cars")
            elif action == "3":
                print("Reserve a car")
            elif action == "4":
                print("Calculate rental costs")
            elif action == "5":
                print("Going back to main menu")
                self.main_menu()
            else:
                print("Invalid input")

    def customer_menu(self):# Not sure how we are going to change from menu to menu.
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
                self.main_menu()
            else:
                print("Invalid input")

    def order_menu(self):# Not sure how we are going to change from menu to menu.
        action = ""
        options = ["1", "2"]
        print("Look up order\n")
        while action not in options: # Need to use the orders file to check if the input matches an order number
            print("Here are your order options:")
            print("1. Look up order\n2. Go back")
            action = input("Enter: ")

            if action == "1":
                order_num = input("Please enter order number: ")
                #if order_num in ## need to use the orders file here
            elif action == "2":
                print("Going back to main menu")
                self.main_menu()
            else:
                print("Invalid input")


### MUST RUN ON NEW_FILE.PY OR ELSE IT WONT RUN