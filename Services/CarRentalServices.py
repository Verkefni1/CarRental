from repositories.CustomerRepository import CustomerRepository
from repositories.ReservationsRepository import ReservationRepository
from repositories.vehicleRepository import VehicleRepository
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

    def search_customer(self,last_name = "", first_name = ""):
        pass    
    
    """ RESERVATIONS MENU FUNCTIONS """
    def new_reservation(self,customer):
        # OPTION 1
        pass
    
    def get_reservation(self,customer):
        # OPTION 2
        pass
    
    def get_all_reservations(self, employee):
        # OPTION 3
        self.__employee_repo.employee_history(employee)
        return self.__reservations_repo.get_all_reservations()

    """ EMPLOYEE MENU FUNCTIONS """
    # OPTION 1
    def employee_change_password(self,employee,new_password):
        self.__employee_repo.change_password(employee,new_password)
    
    # OPTION 2
    def get_all_employees(self):
        pass
    
    # OPTION 3
    def make_admin(self,manager,new_admin):
        if manager.is_manager():
            pass
    
    # OPTION 4
    def get_employee_activity(self,employee):
        pass
    
    # OPTION 5
    def make_new_employee(self,manager):
        pass
    
    # OPTION 6
    def remove_employee(self,manager):
        pass
