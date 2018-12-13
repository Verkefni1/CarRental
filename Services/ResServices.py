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

    #def cancel_res(self, res_number):
    #    return self.__reservation_repo.cancel_res(res_number)

    def check_dates(self, body_type, from_date, to_date):
        return self.__reservation_repo.check_dates(body_type, from_date, to_date)

    #def calc_res_cost(self, body, insurance, length):
    #    return self.__reservation_repo.calc_res_cost(body, insurance, length)

    #def get_payment(self,)