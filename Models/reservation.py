#This is the reservation model

class Reservation:

    def __init__(self, customer, reservation_number, payment_information, start_date, end_date, contract_length, insurance, vehicle_id, employee):
        self.reservation_number = reservation_number
        self.customer = customer
        self.payment_information = payment_information
        self.start_date = start_date
        self.end_date = end_date
        self.contract_length = contract_length
        self.insurance = insurance
        self.vehicle_id = vehicle_id
        self.employee = employee

    def __str__(self):
        return "Reservation number: {}\nCustomer: {}\n Payment information: {}\n Start date: {}\n End date: {}\n Contract length: {}\n Insurance: {}\n Vehicle ID: {}\n Employee: {}\n".format(self.customer, self.reservation_number, self.payment_information, self.start_date, self.end_date, self.contract_length, self.insurance, self.vehicle_id, self.employee)
    
    def get_reservation_number(self):
        return self.reservation_number

    def get_customer(self):
        return self.customer

    def get_payment_information(self):
        return self.payment_information

    def get_start_date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date

    def get_contract_length(self):
        return self.contract_length

    def get_further_insurence(self):
        return self.insurance

    def get_vehicle_id(self):
        return self.vehicle_id

    def get_employee_id(self):
        return self.employee
    