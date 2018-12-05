from Models.Employee import Employee

class EmployeeRepository(object):
    def __init__(self):
        self.__employees = []
    
    def add_employee(self, manager, employee):
        #check manager rank first
        if manager.is_manager():
            with open("./data/employees.csv", "a+") as employees_file:
                username = employee.get_username()
                password = employee.get_password()
                
                employees_file.write("{},{}\n".format(username, password))
    
    def remove_employee(self,manager,employee):
        if manager.is_manager():
            pass

    def get_employees(self):
        if self.__employees == []:
            with open("./data/employees.csv", "r") as employee_file:
                for line in employee_file.readlines():
                    username, password = line.split(",")
                    new_employee = Employee(username, password)
                    self.__employees.append(new_employee)    
        
        return self.__employees


