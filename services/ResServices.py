from models.Reservation import Reservation

from repositories.ReservationsRepository import ReservationRepository
from repositories.vehicleRepository import VehicleRepository

from datetime import datetime


class ResServices():
    def __init__(self):
        #  self.__car_rental_service = ReservationRepository()#remove the repos that we wont need
        #  self.__customer_repo = CustomerRepository()
        self.__vehicle_repo = VehicleRepository()
        self.__reservation_repo = ReservationRepository()

    def make_reservation_class(self, reservation_list):
        """
        Uses reservation as list that was pulled from repo to
        return a Reservation() class object
        """
        try:
            reservation_class = Reservation(reservation_list[0],
                                            reservation_list[1],
                                            reservation_list[2],
                                            reservation_list[3],
                                            reservation_list[4],
                                            reservation_list[5],
                                            reservation_list[6],
                                            reservation_list[7],
                                            reservation_list[8],
                                            reservation_list[9],
                                            reservation_list[10])
            return reservation_class
        except TypeError:
            return "Reservation Not Found"

    def make_res(self, new_res):
        return self.__reservation_repo.make_res(new_res)

    def cancel_res(self, res_number):
        self.__reservation_repo.cancel_reservation(res_number)

    def search_res(self, res_number):
        """
        Searches repository for matching reservation number,
        creates class object using method, and returns that
        so it can be printed from Ui
        """
        search_results = (self.__reservation_repo.
                          search_reservations(res_number))
        class_reservation = self.make_reservation_class(search_results)
        return class_reservation

    def edit_res(self, res_number, edit_action, change):
        return self.__reservation_repo.edit_res(res_number,
                                                edit_action,
                                                change)

    def check_dates(self, body_type, start_date, end_date):
        return self.__reservation_repo.get_reservations()

    def calculate_costs(self, body_type, insurance, res_length):
        # body_type rate is int, insurance rate is a percentage
        total_costs = ""
        if insurance == "y":
            total_costs = (self.get_rate(body_type) * res_length *
                           self.get_rate("insurance"))
        elif insurance == "n":
            total_costs = self.get_rate(body_type) * res_length
        return total_costs

    def get_rate(self, rate_type):
        # fetches rates list from repository
        # and returns the rate value that matches
        # rate_type parameter
        rate_list = self.__reservation_repo.get_rates()

        for rate in rate_list:
            if rate[0] == rate_type:
                return float(rate[1])

    def is_valid_res(self, body, insurance, length):
        total_costs = self.calculate_costs(body, insurance, length)
        if total_costs < 1:
            # Print functions should be in UI
            print("Reservation Length Minimum 1 Day")
            return False
        else:
            print(total_costs)
            return True

    def get_res_length(self, start_date, end_date):
        """
        Gets the difference between the 2 dates in days.
        """
        day1 = datetime.strptime(start_date, '%Y/%m/%d').date()
        day2 = datetime.strptime(end_date, '%Y/%m/%d').date()
        diff = day2 - day1
        res_length = diff.days
        return res_length

    def check_availability(self, body_type, start_date, end_date):
        """
        Compares inventory of selected vehicle body type
        to the number of reservations that both match the body type
        and do not have overlapping dates.
        Returns number of vehicles available
        """
        res_list = self.__reservation_repo.get_reservations()
        inventory = self.count_vehicle_body(body_type)

        start_date = datetime.strptime(start_date, '%Y/%m/%d').date()
        end_date = datetime.strptime(end_date, '%Y/%m/%d').date()

        reserved_inventory = 0  # Number of cars reserved

        for res in res_list:
            if body_type.lower() == res[7].lower():  # res[7] corresponds to vehicle body type
                res_start_date = datetime.strptime(res[4], '%Y/%m/%d').date() # changes the dates from the reservations into datetime info
                res_end_date = datetime.strptime(res[3], '%Y/%m/%d').date()
                # if the selected start date is before a file reservation end date
                # and the selected end date happens before a file reservation,
                # then we know the dates overlap
                if start_date <= res_end_date and end_date >= res_start_date:
                    reserved_inventory += 1
        available = inventory - reserved_inventory
        return available

    def count_vehicle_body(self, body_type):
        """
        Returns inventory of specified
        vehicle body type
        """
        total_inventory = self.__vehicle_repo.get_all_vehicles()
        inventory_body_type = 0

        for vehicle in total_inventory:
            if vehicle[1] == body_type:
                inventory_body_type += 1
        return inventory_body_type

    def display_available_vehicles(self):
        """
        Returns list of number of
        available vehicles
        for current day
        """

        current_day = self.current_day_str()

        rate_list = self.__reservation_repo.get_rates() # Used to get body names
        # Suv, hatchback, sedan
        
        count = 0
        available = []

        for rate in rate_list[0:-1]: #  last value is insurance, and not counted
            count = self.check_availability(
                                      rate[0], current_day,
                                      current_day)
            available.append(count)
            available.append(rate[0])
        return available

    def display_reserved_vehicles(self):
        """
        Returns list of unavailable vehicles
        for current day
        """
        rate_list = self.__reservation_repo.get_rates()
        res_list = self.__reservation_repo.get_reservations()
        matching_res = []
        res_class_list = []

        for rate in rate_list[0:-1]:
            for res in res_list:
                if rate[0].lower() == res[7].lower():
                    matching_res.append(res)
        for res in matching_res:
            res_class_list.append(self.make_reservation_class(res))

        return res_class_list

    def current_day_str(self):
        current_date = datetime.today()
        year = current_date.year
        month = current_date.month
        day = current_date.day
        current_date_str = "{}/{}/{}".format(year, month, day)
        return current_date_str

    def make_reservation_number(self):
        res_list = self.__reservation_repo.get_reservations()
        max_number = 0
        for res in res_list:
            if int(res[0]) > max_number:
                max_number = int(res[0])
        return max_number + 1

    def get_rates_list(self):
        return self.__reservation_repo.get_rates()
