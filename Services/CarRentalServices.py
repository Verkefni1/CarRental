from repositories.customerRepository import CustomerRepository
from repositories.ReservationRepository import ReservationRepository
from repositories.vehicleRepository import VehicleRepository


class CarRentalServices():
     
    def __init__(self):
        self.__car_rental_service = ReservationRepository()
        self.__customer_repo = CustomerRepository()
        self.__vehicle_repo = VehicleRepository()

    def add_customer(self, employee, customer):
        return self.__customer_repo.add_customer(customer)
    
    def add_vehicle(self, employee, manager):
        '''add vehicle to database?'''
        if manager.is_manager():
            return self.__vehicle_repo.add_vehicle()
    
    def get_vehicle(self, employee):
        return self.__vehicle_repo.get_vehicle()
    
    def get_all_vehicles(self, employee):
        return self.__vehicle_repo.get_all_vehicles()

    def get_all_reservations(self, employee):
        return self.__car_rental_service.get_all_reservations()