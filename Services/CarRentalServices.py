from models.Employee import Employee
from models.customer import Customer
from models.Vehicle import Vehicle
from models.reservation import Reservation

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
     
    def write_employee_history(self,employee):
        """ Can be called from methods within services
        to add to employee, car, or whatever we need history"""
        pass
        
    def get_vehicle(self, vehicle_ID):
        return self.__vehicle_repo.get_vehicle(vehicle_ID)
    
    def get_all_vehicles(self, employee):
        return self.__vehicle_repo.get_all_vehicles()

    
    ''' VEHICLE MENU FUNCTIONS '''
    def get_vehicles_by_availability(self,employee):
        # Needs a loop that pulls all clean vehicles first, 
        # then all dirty ones, then all OOO ones
        pass
    
    def get_vehicle_history(self,employee,vehicle_ID):
        # returns all history of a particular vehicle
        pass
    
    def change_vehicle_status(self,employee,vehicle_ID):
        # allows vehicle status to be changed. 
        # Clean, dirty, or OOO?
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

    def search_customer(self,last_name = "", first_name = ""):
        pass    
    
    """ RESERVATIONS FUNCTIONS """
    def new_reservation(self,customer):
        # OPTION 1
        pass
    
    def get_reservation(self,customer):
        # OPTION 2
        pass
    
    def get_all_reservations(self, employee):
        # OPTION 3
        #self.__employee_repo.employee_history(employee)
        return self.__reservations_repo.get_all_reservations()
    
    def calculate_costs(self,body_type,insurance,res_length):
        # body_type rate is int, insurance rate is a percentage
        total_costs = ""
        if insurance == True:
            total_costs = self.get_rate(body_type) * self.get_rate("insurance") * res_length
        elif insurance == False:
            total_costs = self.get_rate(body_type) * res_length
        return total_costs
        

    def get_rate(self,rate_type):
        # fetches rates list from repository
        # and returns the rate value that matches
        # rate_type parameter
        rate_list = self.__reservations_repo.get_rates()

        for rate in rate_list:
            if rate[0] == rate_type:
                return float(rate[1])
