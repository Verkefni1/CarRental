from repositories.CustomerRepository import CustomerRepository
from repositories.ReservationsRepository import ReservationRepository
from repositories.vehicleRepository import VehicleRepository
from models.Employee import Employee


class CarRentalServices():

    def __init__(self):
        self.__car_rental_service = ReservationRepository()
        self.__customer_repo = CustomerRepository()
        self.__vehicle_repo = VehicleRepository()

    def add_customer(self, employee, customer):
        return self.__customer_repo.add_customer(customer)

    def add_vehicle(self, employee, manager, vehicle):
        '''add vehicle to database?'''
        if manager.is_manager():
            self.__vehicle_repo.add_vehicle(vehicle)

    def get_vehicle(self, employee):
        return self.__vehicle_repo.get_vehicle()

    def get_all_vehicles(self, employee):
        return self.__vehicle_repo.get_all_vehicles()

    def get_all_reservations(self, employee):
        return self.__car_rental_service.get_all_reservations()

       def __init__(self):
        self.__customer_repo = CustomerRepository()

    def add_customer(self, employee, customer):
        return self.__customer_repo.add_customer(customer)

    def search_customer(self,last_name = "", first_name = ""):
        return self.__customer_repo.search_customer(last_name, first_name)  
    
    def search_customer_by_kennitala(self, kennitala):
        return self.__customer_repo.search_customer_by_kennitala(kennitala)

    def remove_customer(self, kennitala):
        return self.__customer_repo.remove_customer(kennitala)

    def update_customer(self, kennitala, customer):
        return self.__customer_repo.update_customer(kennitala, customer)
    
    def get_all_customers(self):
        return self.__customer_repo.get_all_customers()
