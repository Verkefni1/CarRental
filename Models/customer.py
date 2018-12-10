class Customer:

    def __init__(self, last_name, first_name, address, drivers_license, kennitala,
                current_rental_order_number=0):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.drivers_license = drivers_license
        self.kennitala = kennitala
        self.current_rental_order_number = current_rental_order_number
    
    def __str__(self):
        return "Customer:\n Full name: {}\n Address: {}\n Drivers license: {}\n Kennitala: {}\n Current rental order number: {}".format(self.first_name + " " + self.last_name, self.address, 
                 self.drivers_license, self.kennitala, self.current_rental_order_number)

    def get_last_name(self):
        return self.last_name
    
    def get_first_name(self):
        return self.first_name
    
    def get_address(self):
        return self.address
    
    def get_drivers_license(self):
        return self.drivers_license
    
    def get_kennitala(self):
        return self.kennitala
    
    def get_current_rental_order_number(self):
        return self.current_rental_order_number
