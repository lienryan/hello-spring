class Person:

    def __init__(self, first_name, status):
        self.first_name = first_name
        self.status = status

    def get_first_name(self):
        return self.first_name

    def get_status(self):
        return self.status

    def set_first_name(self, name):
        self.first_name = name

    def set_status(self, status):
        self.status = status
