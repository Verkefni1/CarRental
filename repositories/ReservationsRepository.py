import csv
import os
from Models.reservation import Reservation

class ReservationRepository:

    def __init__(self):
        self.__reservations = []

    # Add a new reservation
    def add_reservation(self, reservation):
        with open("Reservations.csv", "a+") as reservations_file:
            reservation_number = reservation.get_reservation_number()
            customer = reservation.get_customer()
            payment_information = reservation.get_payment_information()
            start_date = reservation.get_start_date()
            end_date = reservation.get_end_date()
            contract_length = reservation.get_contract_length()
            insurance = reservation.get_further_insurence()
            vehicle_id = reservation.get_vehicle_id()
            employee = reservation.get_employee_id()
            reservations_file.write("{},{},{},{},{},{},{},{},{}\n".format(reservation_number, customer, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee))

    # returns reservation if found, None if not found
    def get_reservation(self, res_number):
            with open("Reservations.csv", "r") as reservation_file:
                for line in reservation_file.readlines():
                    reservation_number, customer, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee = line.split(",")
                    if res_number == reservation_number:
                        foundRes = Reservation(reservation_number, customer, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee)
                        return foundRes
            return None
    
    def edit_reservation(self, reservation_number, reservation):
        with open("Reservations.csv", "r") as reservation_file:
            reader = csv.reader(reservation_file)
            with open("ReservationsTMP.csv", "w+") as reservation_file_tmp:
                writer = csv.writer(reservation_file_tmp)
                for row in reader:
                    if row[0] == reservation_number:
                        res = [ reservation_number, reservation.get_customer(), reservation.get_payment_information(), reservation.get_start_date(), reservation.get_end_date(), reservation.get_contract_length(), reservation.get_further_insurence(), reservation.get_vehicle_id(), reservation.get_employee_id()]
                        writer.writerow(res)
                    else:
                        writer.writerow(row)
        os.rename('ReservationsTmp.csv', 'Reservations.csv')

    def remove_reservation(self, reservation_number):
        with open("Reservations.csv", 'r') as reservation_file:
            reader = csv.reader(reservation_file)
            with open("ReservationsTmp.csv", 'w+') as reservation_file_tmp:
                writer = csv.writer(reservation_file_tmp)
                for row in reader:
                    if row[0] != reservation_number:
                        writer.writerow(row)
        os.rename('ReservationsTmp.csv', 'Reservations.csv')


    
