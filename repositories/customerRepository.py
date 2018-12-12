import csv
import os
from models.customer import Customer

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

    def get_customer(self):
        if self.__customer == []:
            with open("Customer.csv", "r") as customer_file:
                for line in customer_file.readlines():
                    first_name, last_name, address, drivers_license, kennitala = line.split(",")
                    new_customer = Customer(first_name, last_name, address, drivers_license, kennitala)
                    self.__customer.append(new_customer)    
        return self.__customer 
    
    def remove_customer(self, kennitala):
        with open("Customer.csv", 'r') as customer_file:
            reader = csv.reader(customer_file)
            with open("customerTmp.csv", 'w+') as customer_file_tmp:
                writer = csv.writer(customer_file_tmp)
                for row in reader:
                    if row[0] != kennitala:
                        writer.writerow(row)
        os.rename('customerTmp.csv', 'Customer.csv')
                

    


        

    
