class Person(object):

    def __init__(self):
        self.name = ""
        self.phone_number = ""
        self.email_id = ""
        self.city = ""

    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def set_email_id(self, email_id):
        self.email_id = email_id

    def get_email_id(self):
        return self.email_id

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city


if __name__ == '__main__':
    p = Person()
    p.set_city("hyd")
    p.set_name("abc")
    print(p.get_city())
    print(p.get_name())