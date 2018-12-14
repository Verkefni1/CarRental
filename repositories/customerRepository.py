import csv
import os
from models.customer import Customer


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
            ssn = customer.get_ssn()
            current_rental_number = customer.get_current_rental_number()
            customers_file.write("{}, {}, {}, {}, {}, {}\n".format(
                first_name, last_name, address,
                drivers_license, ssn, current_rental_number))

    # returns customer details if found, returns NONE if the customer is not
    # in the system
    def search_customer_by_name(self, last_name="", first_name=""):
        with open("./Data/Customer.csv", "r") as customer_file:
            for line in customer_file.readlines():
                f_name, l_name, address, drivers_license, ssn,
                current_rental_number = line.split(",")
                if l_name == last_name and f_name == first_name:
                    foundCust = Customer(
                        l_name, f_name, address, drivers_license,
                        ssn, current_rental_number)
                    return foundCust
        return None

    # returns customer details if found, returns NONE if the customer is not
    # in the system
    def search_customer_by_ssn(self, ssn):
        with open("./Data/Customer.csv", "r") as customer_file:
            for line in customer_file.readlines():
                f_name, l_name, address, drivers_license, kt,
                current_rental_number = line.split(",")
                if ssn == kt:
                    foundCust = Customer(
                        l_name, f_name, address, drivers_license,
                        kt, current_rental_number)
                    return foundCust
        return None

    # removes customer if they exist in the customer file
    def remove_customer(self, ssn):
        with open("./Data/Customer.csv", 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open("./Data/customerTmp.csv", 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for row in reader:
                    if row[4] != ssn:
                        writer.writerow(row)
        os.rename('./Data/customerTmp.csv', './Data/Customer.csv')

    # updates customer if exists in the customer file.
    # Search for customer by entering the customers kennitala
    def update_customer(self, ssn, edit_action, change):
        with open("./data/Customer.csv", 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open("./data/customerTmp.csv", 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for cus in reader:
                    if ssn == cus[4]:
                        if edit_action == "1":
                            cus = [change, cus[1], cus[2], cus[3],
                                   cus[4], cus[5]]
                        elif edit_action == "2":
                            cus = [cus[0], change, cus[2], cus[3],
                                   cus[4], cus[5]]
                        elif edit_action == "3":
                            cus = [cus[0], cus[1], change, cus[3],
                                   cus[4], cus[5]]
                        elif edit_action == "4":
                            cus = [cus[0], cus[1], cus[2], change,
                                   cus[4], cus[5]]
                        elif edit_action == "5":
                            cus = [cus[0], cus[1], cus[2], cus[3],
                                   cus[4], change]
                        elif cus == []:
                            pass
                        else:
                            writer.writerow(cus)
        os.remove('"./data/customer.csv"')
        os.rename('./data/customerTmp.csv', './data/customer.csv')

    # Prints out all customers in the customer file
    def get_all_customers(self):
        with open("Customer.csv", 'r') as customer_file:
            for row in customer_file:
                return row
