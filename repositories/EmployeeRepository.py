from Models.Employee import Employee
import csv
import os

class EmployeeRepository(object):
    """ 
    Repository classes work directly with the csv files. They take care of reading/writing
    the data and formatting it in a way that's easy for the upper Services/Domain layer to understand
    and work with. 
    """
    def __init__(self):
        self.__employees = []
    
    def make_new_employee(self, employee):
        """Appends the passed employee class into the employee csv file
        """
        with open("./data/employees.csv", "a+") as employees_file:
            username = employee.get_username()
            password = "password"
            admin = False
            employees_file.write("{},{},{}\n".format(username,password,admin))
    
    def remove_employee(self,manager,employee):
        
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
    
    def make_admin(self,employee):
        """ Rewrites the employee file and changes the Manager value of the passed employee to be True.
        """
        with open("Employees.csv", 'r') as employee_file:
            reader = csv.reader(employee_file)
            with open("EmployeesTmp.csv", 'w') as employee_file_tmp:
                writer = csv.writer(employee_file_tmp)
                for row in reader:
                    if row[0] == employee.username:
                        row[2] = True
        os.rename('EmployeesTmp.csv', 'Employees.csv')
    
    def change_password(self,employee,new_password):
        """ Allows the user to rewrite the password value for that employee in the
        employee csv file. Ui prompts user for values, Services checks the user names
        match, Repository commits actual changes
        """
        with open("Employees.csv", 'r') as employee_file:
            reader = csv.reader(employee_file)
            with open("EmployeesTmp.csv", 'w') as employee_file_tmp:
                writer = csv.writer(employee_file_tmp)
                for row in reader:
                    if row[0] == employee.username:
                        row[1] = new_password
        os.rename('EmployeesTmp.csv', 'Employees.csv')

    def get_employees(self):
        """ returns a list with all current employees, except for passwords
        """
        if self.__employees == []:
            with open("./data/employees.csv", "r") as employee_file:
                for line in employee_file.readlines():
                    username, password, manager = line.split(",")
                    #new_employee = Employee(username, password)
                    self.__employees.append(username)
                    # self.__employees.append(manager)    
        
        return self.__employees
    
        




