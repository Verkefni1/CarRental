import csv
import os
from models.Reservation import Reservation

class ReservationRepository:

    def __init__(self):
        self.__reservations = []

    # Add new reservation 
    def new_reservation(self, reservation):
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

    # Displays all reservations in the system
    def get_all_reservations(self):
        if self.__reservations == []:
            with open("./Data/Reservations.csv", "r") as reservation_file:
                for line in reservation_file.readlines():
                    customer, reservation_number, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee = line.split(",")
                    new_reservation = Reservation(
                        customer, reservation_number, payment_information,
                        start_date, end_date, contract_length,
                        insurance, vehicle_id, employee)
                    self.__reservations.append(new_reservation)
        return self.__reservations
    
    # finds reservation by reservation number if in the system 
    def get_reservation(self, res_number):
        with open("./Data/Reservations.csv", "r") as reservation_file:
            for line in reservation_file.readlines():
                customer, reservation_number, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee = line.split(",")
                if res_number == reservation_number:
                    foundRes = Reservation(
                        customer, reservation_number, payment_information,
                        start_date, end_date, contract_length,
                        insurance, vehicle_id, employee)
                    return foundRes
        return None 
 
    # if the reservation is not found it returns None ?
    def edit_reservation(self, reservation_number, reservation):
        with open("./Data/Reservations.csv", "r") as reservation_file:
            reader = csv.reader(reservation_file)
            with open("./Data/ReservationsTMP.csv", "w+") as reservation_file_tmp:
                writer = csv.writer(reservation_file_tmp)
                for row in reader.readlines():
                    if row[1] == reservation_number:
                        res = [ reservation.customer(),
                        reservation.reservation_number(),
                        reservation.payment_information(),
                        reservation.start_date(),
                        reservation.end_date(),
                        reservation.contract_length(),
                        reservation.insurance(),
                        reservation.vehicle_id(), 
                        reservation.employee() ]
                        writer.writerow(res)
                    else:
                        writer.writerow(row)
        os.rename("./Data/ReservationsTMP.csv", "./Data/Reservations.csv")

    # Removes reservation if found in the system
    def remove_reservation(self, reservation_number):
        with open("./Data/Reservations.csv", 'r') as reservation_file:
            reader = csv.reader(reservation_file)
            with open("./Data/ReservationsTmp.csv", 'w+') as reservation_file_tmp:
                writer = csv.writer(reservation_file_tmp)
                for row in reader:
                    if row[1] != reservation_number:
                        writer.writerow(row)
        os.rename('./Data/ReservationsTmp.csv', './Data/Reservations.csv')