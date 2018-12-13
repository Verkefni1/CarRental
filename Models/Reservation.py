class Reservation:

    def __init__(self, reservation_number, customer_license, CC, from_date, to_date, insurance, body_type, current_employee):
        self.reservation_number = reservation_number
        self.customer_license = customer_license
        self.CC = CC
        self.from_date = from_date
        self.to_date = to_date
        self.insurance = insurance
        self.body_type = body_type
        self.employee = current_employee

    #0,customer_license_num,CC_number,from_date,to_date,insurance(Y/N),body,employee

    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.reservation_number, self.customer_license, self.CC, self.from_date, self.to_date, self.insurance, self.body_type, self.employee)

    def get_customer_license(self):
        return self.customer_license
    
    def get_reservation_number(self):
        return self.reservation_number

    def get_CC(self):
        return self.CC

    def get_from_date(self):
        return self.from_date

    def get_to_date(self):
        return self.to_date

    #def get_contract_length(self):
    #    return self.contract_length

    def get_insurance(self):
        return self.insurance

    def get_body_type(self):
        return self.body_type

    def get_employee(self):
        return self.employee