import csv
import os
from models.Reservation import Reservation

class ReservationRepository:
    def __init__(self):
        self.__reservations = []

#customer og employee, I don't know if they should be here! inside add reservation(#,#)
# If they are supposed to be here, then we need to check if user is manager!
    #def add_reservation(self, reservation, customer, employee):
    #    with open("../data/reservations.csv", "a+") as reservations_file:
    #        customer = reservation.get_customer()
    #        reservation_number = reservation.get_reservation_number()
    #        payment_information = reservation.get_payment_information()
    #        start_date = reservation.get_start_date()
    #        end_date = reservation.get_end_date()
    #        contract_length = reservation.get_contract_length()
    #        insurance = reservation.get_insurance()
    #        vehicle_id = reservation.get_vehicle_id()
    #        employee = reservation.get_employee()

    #0,customer_license_num,CC_number,from_date,to_date,insurance(Y/N),body,employee

    def make_res(self, new_res):
        with open("../data/reservations.csv", "a+") as reservations_file:
            customer_license = new_res.get_customer_license()
            CC = new_res.get_CC()
            from_date = new_res.get_from_date()
            to_date = new_res.get_to_date()
            insurance = new_res.get_insurance()
            body_type = new_res.get_body_type()
            employee = new_res.get_employee()
            reservations_file.write("\n{},{},{},{},{},{},{}".format(customer_license, CC, from_date, to_date, insurance, body_type, employee))

    def get_all_reserved(self): #FINAL BUT NEEDS POLISHING
        with open("../data/reservations.csv", "r") as reservation_file:#Prints all the reservations
            reader = csv.reader(reservation_file)
            print("Res Number - Drivers License - Credit Card - From - To - Insurance - Body - Employee")
            for line in reader:
                print(line)

    def search_res(self, res_num): #FINAL BUT NEEDS POLISHING
        with open("../data/reservations.csv", "r") as reservations_file:
            reader = csv.reader(reservations_file)#Prints the reservation with the same reservation number
            for res in reader:
                if res_num == res[0]:
                    print(res)

#Don't know what comes here completely.
#    def get_reservation(self):
#        if self.__reservations == []:
#            with open("./data/reservations.csv", "r") as reservation_file:

#Also confused with this part.
#    def remove_reservation(self):
#        pass

    #0,customer_license_num,CC_number,from_date,to_date,insurance(Y/N),body,employee
    #1. License number\n2. Credit Card\n3. From Date\n4. To Date\n5. Insurance\n6. Body\n7. Finish")#

    def edit_res(self, res_num, edit_action, change):
        with open("../data/reservations.csv", "r") as reservations_file:
            reader = csv.reader(reservations_file)
            with open("../data/reservationsTmp.csv", 'w', newline='') as reservations_tmp_file:
                writer = csv.writer(reservations_tmp_file)
                for res in reader:# Still need to error check if there is no reservation with the same res_num
                    if res_num == res[0]:#if the res_num matches the reservations number the it does one of these actions
                        if edit_action == "1":#each function changes a different part of the reservation depending on the user choice
                            res = [res[0],change,res[2],res[3],res[4],res[5],res[6],res[7]]
                            writer.writerow(res)
                        elif edit_action == "2":
                            res = [res[0],res[1],change,res[3],res[4],res[5],res[6],res[7]]
                            writer.writerow(res)
                        elif edit_action == "3":
                            res = [res[0],res[1],res[2],change,res[4],res[5],res[6],res[7]]
                            writer.writerow(res)
                        elif edit_action == "4":
                            res = [res[0],res[1],res[2],res[3],change,res[5],res[6],res[7]]
                            writer.writerow(res)
                        elif edit_action == "5":
                            res = [res[0],res[1],res[2],res[3],res[4],change,res[6],res[7]]
                            writer.writerow(res)
                        elif edit_action == "6":
                            res = [res[0],res[1],res[2],res[3],res[4],res[5],change,res[7]]
                            writer.writerow(res)
                    elif res == []:
                        pass
                    else:
                        writer.writerow(res)
        os.remove('../data/reservations.csv')
        os.rename('../data/reservationsTmp.csv', '../data/reservations.csv')
    #
    #def retire_vehicle(self, ID):# DOESNT WORK
    #    with open("../data/vehicle.csv", 'r') as vehicle_file:
    #        reader = csv.reader(vehicle_file)
    #        with open("../data/vehicleTmp.csv", 'w') as vehicle_file_tmp:
    #            writer = csv.writer(vehicle_file_tmp)
    #            for row in reader:
    #                if row[0] != ID:
    #                    writer.writerow(row)
    #    os.rename('EmployeesTmp.csv', 'Employees.csv')


                    

    #def make_res(self, drivers_license, body, from_date, to_date):
    #    with open("../data/reservations.csv", "a+") as reservations_file:
    #        drivers

    def check_dates(self, body_type, from_date, to_date): # FINAL
        """ This function opens up the reservations file to count how many cars are reserved of the requested body_type
        it then takes the dates for those cars to see if any of them finish their reservation
        time before the time the current customer wants to rent a car.
        Body_amount tells us how many cars of this body are in the reservations file
        Remaining tells us how many cars of this type are available because they aren't in the reservations file
        Available_count determines how many cars are reserved that will become available by the time we want to reserve a
        car of that body at a certain time. it then adds the remaining cars to get a total count of available cars.
        """
        available_count = 0
        body_amount = 0
        with open("../data/reservations.csv", "r") as reservations_file:
            reader = csv.reader(reservations_file)
            for car in reader:
                if body_type == car[6]:#car[6] gives the body type
                    body_amount += 1
                    if from_date >= car[4]:#car[4] gives the to_date for the car. if it finishes being rented out before the time 
                                           #I want to rent the car then it is available
                        available_count += 1
        remaining = 10 - body_amount #body_amount counts how many cars of this type are in the reservations data file
        available_count += remaining # since we will only have 30 cars, 10 of each type remaining tells us how many cars of this type
        return available_count       # are available. we then add the remaining cars to the availabe count