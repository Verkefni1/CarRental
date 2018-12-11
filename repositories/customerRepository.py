import csv
import os
from models.Customer import Customer

class CustomerRepository:

    def __init__(self):
        self.__customer = []

    def add_customer(self, customer):
        with open("Customer.csv", "a+") as customers_file:
            first_name = customer.get_first_name()
            last_name = customer.get_last_name()
            address = customer.get_address()
            drivers_license = customer.get_drivers_license()
            kennitala = customer.get_kennitala()
            current_rental_number = customer.get_current_rental_number()
            customers_file.write("{}, {}, {}, {}, {}, {}\n".format(first_name, last_name, address,
                                                        drivers_license, kennitala, current_rental_number))
    # returns customer if found, None if not
    def search_customer_by_name(self,last_name = "", first_name = ""):
        with open("Customer.csv", "r") as customer_file:
            for line in customer_file.readlines():
                f_name,l_name,address,drivers_license, kennitala, current_rental_number = line.split(",")
                if l_name == last_name and f_name == first_name:
                    foundCust = Customer(l_name,f_name,address,drivers_license, kennitala, current_rental_number)
                    return foundCust
        return None 

    # returns customer if found, None if not
    def search_customer_by_kennitala(self, kennitala):
        with open("Customer.csv", "r") as customer_file:
            for line in customer_file.readlines():
                f_name,l_name,address,drivers_license, kt, current_rental_number = line.split(",")
                if kennitala == kt:
                    foundCust = Customer(l_name,f_name,address,drivers_license, kt, current_rental_number)
                    return foundCust
        return None 

    # removes customer if exists in file
    def remove_customer(self, kennitala):
        with open("Customer.csv", 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open("customerTmp.csv", 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for row in reader:
                    if row[4] != kennitala:
                        writer.writerow(row)
        os.rename('customerTmp.csv', 'Customer.csv')
                

    


        

    
