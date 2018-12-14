import csv
import os
from Models.customer import Customer


class CustomerRepository:

    def __init__(self):
        self.__customer = []

    # Adds customer into customer file
    def add_customer(self, customer):
        with open("./data/customer.csv", "a+") as customers_file:
            first_name = customer.get_first_name()
            last_name = customer.get_last_name()
            address = customer.get_address()
            ssn = customer.get_ssn()
            drivers_license = customer.get_drivers_license()
            current_rental_number = customer.get_current_rental_number()
            customers_file.write("{},{},{},{},{},{}\n".format(
                first_name, last_name, address,
                ssn, drivers_license, current_rental_number))

        # Prints out all customers in the customer file
    def get_all_customers(self):
        self.__customer == []
        with open("./data/customer.csv", "r") as customer_file:
            reader = csv.reader(customer_file)
            for line in reader:
                self.__customer.append(line)
        return self.__customer

    # returns customer details if found, returns NONE if the customer is not
    # in the system
    def search_customer_by_ssn(self, ssn):
        with open("./data/customer.csv", "r") as customer_file:
            reader = csv.reader(customer_file)
            for customer in reader:
                if customer[4] == ssn:
                    return customer
        return None

    # updates customer if exists in the customer file.
    # Search for customer by entering the customers kennitala
    def edit_customer(self, ssn, edit_action, change):
        with open('./data/customer.csv', 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open('./data/customerTmp.csv', 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for cus in reader:
                    if ssn == cus[4]:
                        if edit_action == "1":
                            cus = [change, cus[1], cus[2], cus[3],
                                   cus[4], cus[5]]
                            writer.writerow(cus)
                        elif edit_action == "2":
                            cus = [cus[0], change, cus[2], cus[3],
                                   cus[4], cus[5]]
                            writer.writerow(cus)
                        elif edit_action == "3":
                            cus = [cus[0], cus[1], change, cus[3],
                                   cus[4], cus[5]]
                            writer.writerow(cus)
                        elif edit_action == "4":
                            cus = [cus[0], cus[1], cus[2], change,
                                   cus[4], cus[5]]
                            writer.writerow(cus)
                        elif edit_action == "6":
                            cus = [cus[0], cus[1], cus[2], cus[3],
                                   cus[4], change]
                            writer.writerow(cus)
                        elif cus == []:
                            pass
                    else:
                        writer.writerow(cus)
        os.remove('./data/customer.csv')
        os.rename('./data/customerTmp.csv', './data/customer.csv')

    # removes customer if they exist in the customer file
    def remove_customer(self, ssn):
        with open('./data/customer.csv', 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open('./data/customerTmp.csv', 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for row in reader:
                    if row[4] != ssn:
                        writer.writerow(row)
        os.rename('./data/customerTmp.csv', './data/customer.csv')