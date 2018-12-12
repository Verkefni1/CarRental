import csv
import os
from models.reservation import Reservation

class ReservationRepository:

    def __init__(self):
        self.__reservations = []



    def get_rates(self):
        rates_list = []
        with open("./data/rates.csv",'r') as rates_file:
            reader = csv.reader(rates_file)
            for row in reader:
                rates_list.append(row)        
        return rates_list
            


    
