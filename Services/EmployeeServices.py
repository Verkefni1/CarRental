from repositories.EmployeeRepository import EmployeeRepository
from models.Employee import Employee

class EmployeeServices(object):
""" Services takes care of the logic between the Ui and the data held in the Repository. 
    Checking for correct passwords, if user is manager, etc, all done here. """
    
    def __init__(self):
        self.__employee_repo = EmployeeRepository()
    
    def is_employee(self,username):
        for employee in self.__employee_repo.get_employees():
            if employee == username
            return True
        else:
            return False
    
    
    def add_employee(self,manager,employee):
        """ Must check if current user is manager. If True,
        then runs method to add employee
        """
        if manager.is_manager():
            make_new_employee
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
    
    
    def change_password(self,employee,current_password,new_password):
        if employee.get_password() == current_password:
            self.__employee_repo.change_password(employee,new_password)
    
    def login(self,current_employee,password):
        if current_employee.get_password() == password:
            return True

        """ EMPLOYEE MENU FUNCTIONS """
    # OPTION 1
    def employee_change_password(self,employee,new_password):
        self.__employee_repo.change_password(employee,new_password)
    
    # OPTION 2
    def get_all_employees(self):
        return self.__employee_repo.get_employees()
    
    
    # OPTION 3
    def make_admin(self,manager,new_admin):
        if manager.is_manager():
            self.__employee_repo.make_admin(new_admin)
    
    # OPTION 4
    def get_employee_activity(self,employee):
        pass
    
    # OPTION 5
    def make_new_employee(self,manager,username):
        if manager.is_manager():
            self.__employee_repo.make_new_employee(username)
    
    # OPTION 6
    def remove_employee(self,manager,username):
        if manager.is_manager() and self.__employee_repo.is_employee(username):
            self.__employee_repo.remove_employee(username)

    


