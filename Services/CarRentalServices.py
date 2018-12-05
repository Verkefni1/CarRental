from repositories.customerRepository import CustomerRepository
from repositories.EmployeeRepository import EmployeeRepository
from repositories.vehicleRepository import VehicleRepository

class CarRentalServices():
     
    def __init__(self):
        self.__car_rental_service = ReservarionRepository()
        self.__customer_repository = customerRepository()
        self.__vehicle_repository = vehicleRepository()

    def add_customer(self, employee, customer):
        return self.__customer_repository.add_customer(customer)
    
    def add_vehicle(self, employee, manager, customer):
        return self.__vehicle_repository.add_vehicle(customer)
    
    def get_vehicle(self, employee):
        return self.__vehicle_repository.get_vehicle()
    
    def get_all_vehicles(self, employee):
        return self.__vehicle_repository.get_all_vehicles()

    def get_all_reservations(self, employee):
        return self.__car_rental_service.get_all_reservations()