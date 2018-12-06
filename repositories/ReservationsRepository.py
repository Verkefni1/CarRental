import csv
import os
from models.reservation import reservation

class ReservationRepository:

    def __init__(self):
        self.__reservations = []

#customer og employee, I don't know if they should be here! inside add reservation(#,#)
# If they are supposed to be here, then we need to check if user is manager!
    def add_reservation(self, customer, employee):
        with open("./data/reservations.csv", "a+") as reservations_file:
            customer = reservation.get_customer()
            reservation_number = reservation.get_reservation_number()
            payment_information = reservation.get_payment_information()
            start_date = reservation.get_start_date()
            end_date = reservation.get_end_date()
            contract_length = reservation.get_contract_length()
            insurance = reservation.get_insurance()
            vehicle_id = reservation.get_vehicle_id()
            employee = reservation.get_employee()
            reservations_file.write("{}, {}, {}, {}, {}, {}, {}, {}, {}\n".format(customer, reservation_number, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee))

#Don't know what comes here completely.
    def get_reservation(self, customer, employee):
        if self.__reservations == []:
            with open("Reservations.csv", "r") as reservation_file:
                for line in reservation_file.readlines():
                    customer, reservation_number, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee = line.split(",")
                    new_reservation = reservation(customer, reservation_number, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee)
                    self.__reservations.append(new_reservation)
        return self.__reservations

#Also confused with this part.
    def remove_reservation(self, reservation_number):
        with open("Reservations.csv", 'r') as reservation_file:
            reader = csv.reader(reservation_file)
            with open("ReservationsTmp.csv", 'w+') as reservation_file_tmp:
                writer = csv.writer(reservation_file_tmp)
                for row in reader:
                    if row[0] != reservation_number:
                        writer.writerow(row)
        os.rename('ReservationsTmp.csv', 'Reservations.csv')


    
