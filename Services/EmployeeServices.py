from repositories.EmployeeRepository import EmployeeRepository

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
        runs method remove_employee from Repo layer
        """
        if manager.is_manager():
            self.__employee_repo.remove_employee(employee)

