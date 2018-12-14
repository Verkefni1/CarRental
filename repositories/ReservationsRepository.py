import csv
import os
from models.reservation import Reservation


class ReservationRepository:
    def __init__(self):
        self.__reservations = []

    def get_rates(self):
        rates_list = []
        with open("./data/rates.csv", 'r') as rates_file:
            reader = csv.reader(rates_file)
            for row in reader:
                rates_list.append(row)        
        return rates_list

    def make_res(self, new_res):
        with open("./data/reservations.csv", "a+") as reservations_file:
            customer_license = new_res.get_customer_license()
            reservation_number = new_res.get_reservation_number()
            credit_card = new_res.get_CC()
            from_date = new_res.get_from_date()
            to_date = new_res.get_to_date()
            insurance = new_res.get_insurance()
            payment_method = new_res.get_payment_method()
            body_type = new_res.get_body_type()
            employee = new_res.get_employee()
            reservations_file.write("\n{},{},{},{},{},{},{},{},{}".format(
                                    reservation_number, customer_license,
                                    credit_card, from_date, to_date, insurance,
                                    payment_method, body_type, employee))

    def get_all_reserved(self):  # FINAL BUT NEEDS POLISHING
        with open("./data/reservations.csv", "r") as reservation_file: #P rints all the reservations
            reader = csv.reader(reservation_file)
            print("Res Number - Drivers License - Credit Card - From - To - Insurance - Body - Employee") ## Needs to be in UI
            for line in reader:
                print(line)

    def search_reservations(self, res_num): #FINAL BUT NEEDS POLISHING
        with open("./data/reservations.csv", "r") as reservations_file:
            reader = csv.reader(reservations_file)#Prints the reservation with the same reservation number
            for reservation in reader:
                if res_num == reservation[0]:
                    return reservation

    def edit_res(self, res_num, edit_action, change):
        with open("./data/reservations.csv", "r") as reservations_file:
            reader = csv.reader(reservations_file)
            with open("./data/reservationsTmp.csv", 'w',
                      newline='') as reservations_tmp_file:
                writer = csv.writer(reservations_tmp_file)
                for res in reader:  # Still need to error check if there is no reservation with the same res_num
                    if res_num == res[0]:  # if the res_num matches the reservations number the it does one of these actions
                        if edit_action == "1":  # each function changes a different part of the reservation depending on the user choice
                            res = [res[0], change, res[2], res[3],
                                   res[4], res[5], res[6], res[7]]
                            writer.writerow(res)
                        elif edit_action == "2":
                            res = [res[0], res[1], change, res[3],
                                   res[4], res[5], res[6], res[7]]
                            writer.writerow(res)
                        elif edit_action == "3":
                            res = [res[0], res[1], res[2], change,
                                   res[4], res[5], res[6], res[7]]
                            writer.writerow(res)
                        elif edit_action == "4":
                            res = [res[0], res[1], res[2], res[3],
                                   change, res[5], res[6], res[7]]
                            writer.writerow(res)
                        elif edit_action == "5":
                            res = [res[0], res[1], res[2], res[3],
                                   res[4], change, res[6], res[7]]
                            writer.writerow(res)
                        elif edit_action == "6":
                            res = [res[0], res[1], res[2], res[3],
                                   res[4], res[5], change, res[7]]
                            writer.writerow(res)
                    elif res == []:
                        pass
                    else:
                        writer.writerow(res)
        os.remove('./data/reservations.csv')
        os.rename('./data/reservationsTmp.csv', './data/reservations.csv')

    def get_reservations(self):
        """
        Returns list of lists of all reservations
        """
        res_list = []
        with open("./data/reservations.csv", "r") as reservations_file:
            reader = csv.reader(reservations_file)
            for row in reader:
                res_list.append(row)
        return res_list

    def cancel_reservation(self, resID):
        """
        Compares parameter reservation IDnumber to those in vehicle data file
        and removes reservation with IDnumber match, of which there should
        only be one.
        """
        with open("./data/reservations.csv", "r") as reservations_file:
            reader = csv.reader(reservations_file)
            with open("./data/reservations_temp.csv", "w+",
                      newline='') as reservations_temp:
                writer = csv.writer(reservations_temp)
                for row in reader:
                    if row[0] != resID:
                        writer.writerow(row)
        os.remove('./data/reservations.csv')
        os.rename('./data/reservations_temp.csv', './data/reservations.csv')
