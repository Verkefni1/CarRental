from repositories.ReservationRepository import ReservationRepository

class ResServices():
    def __init__(self):
        #self.__car_rental_service = ReservationRepository()#remove the repos that we wont need
        #self.__customer_repo = CustomerRepository()
        #self.__vehicle_repo = VehicleRepository()
        self.__reservation_repo = ReservationRepository()

    def make_res(self, new_res):##
        return self.__reservation_repo.make_res(new_res)

    def search_res(self, res_number):
        return self.__reservation_repo.search_res(res_number)

    def edit_res(self, res_number, edit_action, change):
        return self.__reservation_repo.edit_res(res_number, edit_action, change)

    def get_res_length(self, from_date, to_date):#Gets the difference between the 2 dates in days.
        day1 = datetime.strptime(from_date, '%Y/%m/%d').date()
        day2 = datetime.strptime(to_date, '%Y/%m/%d').date()
        diff = day2 - day1
        res_length = diff.days
        return res_length
        #print(diff.days)

    #def cancel_res(self, res_number):
    #    return self.__reservation_repo.cancel_res(res_number)

    def check_availability(self, body_type, from_date):
        res_list = self.__reservation_repo.get_reservations()
        available_count = 0
        body_amount = 0
        for res in res_list:
            if body_type == res[6]:#car[6] gives the body type
                    body_amount += 1
                    if from_date >= res[4]:#car[4] gives the to_date for the car. if it finishes being rented out before the time 
                                           #I want to rent the car then it is available
                        available_count += 1
        remaining = 10 - body_amount #body_amount counts how many cars of this type are in the reservations data file
        available_count += remaining # since we will only have 30 cars, 10 of each type remaining tells us how many cars of this type
        return available_count       # are available. we then add the remaining cars to the availabe count
