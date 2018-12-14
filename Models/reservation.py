class Reservation:

    def __init__(self, reservation_number, customer_license, credit_card, from_date, to_date, insurance, payment_method, body_type, current_employee,vehicleID="Not Picked Up Yet"):
        self.reservation_number = reservation_number
        self.customer_license = customer_license
        self.credit_card = credit_card
        self.from_date = from_date
        self.to_date = to_date
        self.insurance = insurance
        self.payment_method = payment_method
        self.body_type = body_type
        self.employee = current_employee
        self.vehicleID = vehicleID


    def __str__(self):
        return ('Reservation Number: {}\n'
        'Customer License Number: {}\n'
        'Credit Card: ************{}\n'
        'Start Date: {}\n'
        'End Date: {}\n'
        'Insurance: {}\n'
        'Payment Method: {}\n'
        'Vehicle Body Type: {}\n'
        'Vehicle ID Number: {}\n'
        'Employee: {}\n'.format(self.reservation_number,self.customer_license,
        self.hide_credit_card(),self.from_date, self.to_date, self.insurance_bool_as_word(),
        self.payment_method, self.body_type, self.vehicleID, self.employee))

    def get_customer_license(self):
        return self.customer_license
    
    def get_reservation_number(self):
        return self.reservation_number

    def get_CC(self):
        return self.credit_card

    def get_from_date(self):
        return self.from_date

    def get_to_date(self):
        return self.to_date

    def get_insurance(self):
        return self.insurance

    def get_payment_method(self):
        return self.payment_method

    def get_body_type(self):
        return self.body_type

    def get_employee(self):
        return self.employee
    
    def hide_credit_card(self):
        last_four = str(self.credit_card)[-5:-1]
        return last_four
    
    def insurance_bool_as_word(self):
        ins_str = "False"
        if self.insurance == "True":
            ins_str = "Yes"
            return ins_str
        else:
            ins_str = "No"
            return ins_str