import csv
import os
from models.reservation import reservation

class ReservationRepository:

    def __init__(self):
        self.__reservations = []

#customer og employee, I don't know if they should be here! inside add reservation(#,#)
# If they are supposed to be here, then we need to check if user is manager!
    def add_reservation(self, reservation, customer, employee):
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

#Don't know what comes here completely.
    def get_reservation(self):
        if self.__reservations == []:
            with open("./data/reservations.csv", "r") as reservation_file:

#Also confused with this part.
    def remove_reservation(self):
        pass

    
