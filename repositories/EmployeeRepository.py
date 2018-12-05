from Models.Employee import Employee
import csv
import os

class EmployeeRepository(object):
""" Repository classes work directly with the csv files. They take care of reading/writing
the data and formatting it in a way that's easy for the upper Services/Domain layer to understand
and work with. 
"""
    def __init__(self):
        self.__employees = []
    
    def add_employee(self, manager, employee):
        """ first checks if current user is a manager. If it returns True,
        it appends the passed employee class into the employee csv file
        """
        if manager.is_manager():
            with open("./data/employees.csv", "a+") as employees_file:
                username = employee.get_username()
                password = employee.get_password()
                
                employees_file.write("{},{}\n".format(username, password))
    
    def remove_employee(self,manager,employee):
        if manager.is_manager():
            """ first checks if current user is a manager. If it returns True,
            it rewrites the employee csv file to exclude the passed employee class
            by skipping the row that has a matching username in its username column (index 0)
            """
            remove_employee = employee.get_username()
            with open("Employees.csv", 'r') as employee_file:
                reader = csv.reader(employee_file)
                with open("EmployeesTmp.csv", 'w') as employee_file_tmp:
                    writer = csv.writer(employee_file_tmp)
                    for row in reader:
                        if row[0] != remove_employee:
                            writer.writerow(row)
            os.rename('EmployeesTmp.csv', 'Employees.csv')
    
    def make_manager(self,manager,employee):
        """ again, first checks if current user is a manager. If it returns True, 
        it rewrites the employee file and changes the Manager value of the passed employee to be True.
        """
        if manager.is_manager():
            with open("Employees.csv", 'r') as employee_file:
                reader = csv.reader(employee_file)
                with open("EmployeesTmp.csv", 'w') as employee_file_tmp:
                    writer = csv.writer(employee_file_tmp)
                    for row in reader:
                        if row[0] == employee.username:
                            row[3] = True
            os.rename('EmployeesTmp.csv', 'Employees.csv')
    
    def change_password(self,current_user,new_password_employee):
        """ It checks that the current user and the passed employee have the same username.
        If true, it allows the user to rewrite the password value for that employee in the
        employee csv file. current_employee will be passed automatically, new_password_employee
        is inputed by user from Ui
        """
        if current_user.username == new_password_employee.username:
            pass

    def get_employees(self):
        """ returns a list with all current employees, except for passwords
        """
        if self.__employees == []:
            with open("./data/employees.csv", "r") as employee_file:
                for line in employee_file.readlines():
                    username, password = line.split(",")
                    #new_employee = Employee(username, password)
                    self.__employees.append(username)    
        
        return self.__employees


