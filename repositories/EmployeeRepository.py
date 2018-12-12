import csv
import os

from models.Employee import Employee

class EmployeeRepository(object):
    """ 
    Repository classes work directly with the csv files. They take care of reading/writing
    the data and formatting it in a way that's easy for the upper Services/Domain layer to understand
    and work with. 
    """
    def __init__(self):
        self.__employees = []
    
    def make_new_employee(self, username):
        """Appends the passed employee username string into the employee csv file
        """
        with open("./data/employees.csv", "a+") as employees_file:
            employee = username
            password = "pass"
            admin = False
            employees_file.write("\n{},{},{}".format(employee,password,admin))
    
    def remove_employee(self,employee):
        
        """ first checks if current user is a manager. If it returns True,
        it rewrites the employee csv file to exclude the passed employee class
        by skipping the row that has a matching username in its username column (index 0)
        """
        
        with open("./data/employees.csv", 'r') as employee_file:
            reader = csv.reader(employee_file)
            with open("./data/employeesTmp.csv", 'w') as employee_file_tmp:
                writer = csv.writer(employee_file_tmp)
                for row in reader:
                    if row[0] != employee:
                        writer.writerow(row)
        os.rename('./data/employeesTmp.csv', './data/employees.csv')
    

    def get_employees(self):
        """ returns a list with all current employees, except for passwords
        """
        employee_list = []
        with open("./data/employees.csv", "r") as employee_file:
            for line in employee_file.readlines():
                username, password, manager = line.split(",")
                #new_employee = Employee(username, password)
                employee_list.append(username)
                    # self.__employees.append(manager)    
        
        return employee_list
    
    def get_employee_class(self,query_username,query_password):
        """returns employee class if both parameter username and
        password match file entry"""

        if self.__employees == []:
            with open("./data/employees.csv","r") as employee_file:
                for line in employee_file.readlines():
                    username,password,manager = line.split(",")
                    if username == query_username and query_password == password:
                        employee_class = Employee(username,password,manager)
                        return employee_class
    

    def make_admin(self,employee):
        """ Takes in employee username and rewrites the employee file and changes the Manager value of the passed employee to be True.
        """        
        with open("./data/employees.csv", 'r') as employee_file:
            reader = csv.reader(employee_file)
            with open("./data/employeesTmp.csv","w+", newline='') as employee_file_tmp:
                writer = csv.writer(employee_file_tmp)
                for line in reader:
                    #Remove after seeing if it works
                    #line = [part.strip(' ') for part in line]
                    if line[0] == employee:
                        empl = [line[0],line[1],True]
                        writer.writerow(empl)
                    elif line == []:
                        pass
                    else:
                        writer.writerow(line)
        
        os.remove('./data/employees.csv')
        os.rename('./data/employeesTmp.csv', './data/employees.csv')

    
    def employee_change_password(self,employee,new_password):
        """ Takes in employee username and rewrites the employee file and changes the Manager value of the passed employee to be True.
        """        
        with open("./data/employees.csv", 'r') as employee_file:
            reader = csv.reader(employee_file)
            with open("./data/employeesTmp.csv","w+", newline='') as employee_file_tmp:
                writer = csv.writer(employee_file_tmp)
                for line in reader:
                    #Remove after seeing if it works
                    #line = [part.strip(' ') for part in line]
                    if line[0] == employee:
                    
                        empl = [line[0],new_password,line[2]]
                        writer.writerow(empl)
                    elif line == []:
                        pass
                    else:
                        writer.writerow(line)
        
        os.remove('./data/employees.csv')
        os.rename('./data/employeesTmp.csv', './data/employees.csv')


