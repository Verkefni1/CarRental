class Vehicle(object):
    def __init__(self,IDnumber,body,make,model,year,color,transmission):
        self.IDnumber = IDnumber
        self.body = body
        self.make = make
        self. model = model
        self.year = year
        self. color = color
        self.transmission = transmission
    
    def get_IDnumber(self):
        return self.IDnumber
    
    def get_body(self):
        return self.body
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_year(self):
        return self.year
    
    def get_color(self):
        return self.color
    
    def get_transmission(self):
        return self.transmission
