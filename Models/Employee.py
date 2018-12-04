class Employee:
    def __init__(self, username = "", password = "", rank = ""):
        self.username = username
        self.__password = password
        self.rank = rank

    def get_username(self):
        return self.username

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "Username: {}\nRank: {}".format(self.username, self.rank)