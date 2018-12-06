class Employee:
    def __init__(self, username, password = "password", manager = False):
        self.username = username
        self.__password = password
        self.manager = manager

    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.__password

    def is_manager(self):
        return self.manager

    def __str__(self):
        return "Username: {}\nManager: {}".format(self.username, self.manager)