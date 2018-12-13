import csv
import os
from models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.__customer = []

    # Adds customer into customer file
    def add_customer(self, customer):
        with open("./Data/Customer.csv", "a+") as customers_file:
            first_name = customer.get_first_name()
            last_name = customer.get_last_name()
            address = customer.get_address()
            drivers_license = customer.get_drivers_license()
            kennitala = customer.get_kennitala()
            current_rental_number = customer.get_current_rental_number()
            customers_file.write("{}, {}, {}, {}, {}, {}\n".format(
                first_name, last_name, address,
                drivers_license, kennitala, current_rental_number))

    # returns customer details if found, returns NONE if the customer is not in the system
    def search_customer_by_name(self, last_name="", first_name=""):
        with open("./Data/Customer.csv", "r") as customer_file:
            for line in customer_file.readlines():
                f_name, l_name, address, drivers_license, kennitala, current_rental_number = line.split(",")
                if l_name == last_name and f_name == first_name:
                    foundCust = Customer(
                        l_name, f_name, address, drivers_license,
                        kennitala, current_rental_number)
                    return foundCust
        return None

    # returns customer details if found, returns NONE if the customer is not in the system
    def search_customer_by_kennitala(self, kennitala):
        with open("./Data/Customer.csv", "r") as customer_file:
            for line in customer_file.readlines():
                f_name, l_name, address, drivers_license, kt, current_rental_number = line.split(",")
                if kennitala == kt:
                    foundCust = Customer(
                        l_name, f_name, address, drivers_license, 
                        kt, current_rental_number)
                    return foundCust
        return None

    # removes customer if they exist in the customer file. 
    def remove_customer(self, kennitala):
        with open("./Data/Customer.csv", 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open("./Data/customerTmp.csv", 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for row in reader:
                    if row[4] != kennitala:
                        writer.writerow(row)
        os.rename('./Data/customerTmp.csv', './Data/Customer.csv')

    # updates customer if exists in the customer file. 
    # Search for customer by entering the customers kennitala
    def update_customer(self, kennitala, customer):
        with open("./Data/Customer.csv", 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open("./Data/customerTmp.csv", 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for row in reader:
                    print(row)
                    if row[4] == kennitala:
                        cust = [
                            customer.get_first_name(),
                            customer.get_last_name(),
                            customer.get_address(), 
                            customer.get_drivers_license(),
                            customer.get_kennitala(), 0]
                        writer.writerow(cust)
                    else:
                        writer.writerow(row)
        os.rename('./Data/customerTmp.csv', './Data/Customer.csv')

    # Prints out all customers in the customer file
    def get_all_customers(self):
        with open("Customer.csv", 'r') as customer_file:
            for row in customer_file:
                return row


        

    
