from models.Employee import Employee
from models.Customer import Customer
from models.Vehicle import Vehicle
from models.Reservation import Reservation


from repositories.customerRepository import CustomerRepository
from repositories.ReservationsRepository import ReservationRepository
from repositories.vehicleRepository import VehicleRepository
from repositories.EmployeeRepository import EmployeeRepository


class CarRentalServices():

    def __init__(self):
        self.__reservations_repo = ReservationRepository()
        self.__customer_repo = CustomerRepository()
        self.__vehicle_repo = VehicleRepository()
        self.__employee_repo = EmployeeRepository()

    def get_vehicle(self, vehicle_ID):
        return self.__vehicle_repo.get_vehicle(vehicle_ID)

    def get_all_vehicles(self, employee):
        return self.__vehicle_repo.get_all_vehicles()


    ''' VEHICLE MENU FUNCTIONS '''
    def get_vehicles_by_availability(self,employee):
        # Needs a loop that pulls all clean vehicles first, 
        # then all dirty ones, then all OOO ones
        pass

    def add_vehicle(self, vehicle):
        '''receives class'''
        #self.__vehicle_repo.add_vehicle(vehicle)
        pass
    
    def remove_vehicle(self,vehicle):
        """ Remove vehicle from DB"""
        #self.__vehicle_repo.remove_vehicle(vehicle)
        pass

    """ CUSTOMER MENU FUNCTIONS """
    def add_customer(self, employee, customer):
        return self.__customer_repo.add_customer(customer)

    def search_customer_by_name(self, last_name="", first_name=""):
        return self.__customer_repo.search_customer_by_name(
                            last_name, first_name)

    def search_customer_by_ssn(self, ssn):
        return self.__customer_repo.search_customer_by_kennitala(ssn)

    def remove_customer(self, ssn):
        return self.__customer_repo.remove_customer(ssn)

    def update_customer(self, ssn, customer):
        return self.__customer_repo.update_customer(ssn, customer)
    
    def get_all_customers(self):
        return self.__customer_repo.get_all_customers()  

    def is_valid_res(self, body, insurance, length):
        total_costs = self.calculate_costs(body, insurance, length)
        if total_costs < 1:
            # Print functions should be in UI
            print("Reservation Length Minimum 1 Day")
            return False
        else:
            print(total_costs)
            return True
