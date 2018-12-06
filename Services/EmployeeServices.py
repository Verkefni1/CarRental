from repositories.EmployeeRepository import EmployeeRepository
from models.Employee import Employee

class EmployeeServices(object):
""" Services takes care of the logic between the Ui and the data held in the Repository. 
    Checking for correct passwords, if user is manager, etc, all done here. """
    
    def __init__(self):
        self.__employee_repo = EmployeeRepository()
    
    def add_employee(self,manager,employee):
        """ Must check if current user is manager. If True,
        then runs method to add employee
        """
        if manager.is_manager():
            self.__employee_repo.add_employee(employee)
    
    def remove_employee(self,manager,employee):
        """Must check if current user is manager. If True,
        runs method remove_employee from repo layer
        """
        if manager.is_manager():
            self.__employee_repo.remove_employee(employee)
    
    def make_manager(self,manager,employee):
        """Must check if current user is manager. If True,
        runs method make_manager from repo layer
        """
        if manager.is_manager():
            self.__employee_repo.make_manager(employee)
    
    def get_employees(self,manager):
        """ Only managers can see all employees"""
        if manager.is_manager():
            return self.__employee_repo.get_employees()
    
    def change_password(self,employee,current_password,new_password):
        if employee.get_password() == current_password:
            self.__employee_repo.change_password(employee,new_password)
    
    def login(self,current_employee,password):
        if current_employee.get_password() == password:
            return True

