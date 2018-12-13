from repositories.CustomerRepository import CustomerRepository
from repositories.ReservationsRepository import ReservationRepository
from repositories.VehicleRepository import VehicleRepository
from repositories.EmployeeRepository import EmployeeRepository

from models.Employee import Employee


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
        
    def get_vehicle(self, employee):
        return self.__vehicle_repo.get_vehicle()
    
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
        '''add vehicle to database?'''
        self.__vehicle_repo.add_vehicle(vehicle)
    
    def remove_vehicle(self,vehicle):
        """ Remove vehicle from DB"""
        self.__vehicle_repo.remove_vehicle(vehicle)

    """ CUSTOMER MENU FUNCTIONS """
    def add_customer(self, employee, customer):
        return self.__customer_repo.add_customer(customer)

    def search_customer_by_name(self,last_name = "", first_name = ""):
        return self.__customer_repo.search_customer_by_name(last_name, first_name)  
    
    def search_customer_by_ssn(self, ssn):
        return self.__customer_repo.search_customer_by_kennitala(ssn)

    def remove_customer(self, ssn):
        return self.__customer_repo.remove_customer(ssn)

    def update_customer(self, ssn, customer):
        return self.__customer_repo.update_customer(ssn, customer)
    
    def get_all_customers(self):
        return self.__customer_repo.get_all_customers()

    """ RESERVATIONS MENU FUNCTIONS """
    def new_reservation(self, reservation):
        return self.__reservations_repo.new_reservation(reservation)
    
    def get_reservation(self, reservation_number):
        return self.__reservations_repo.get_reservation(reservation_number)
    
    def get_all_reservations(self, employee):
        self.__employee_repo.employee_history(employee)
        return self.__reservations_repo.get_all_reservations()

 
