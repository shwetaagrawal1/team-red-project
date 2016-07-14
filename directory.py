from Person import Person
from json_reader import JSONReader

class Directory:
    providers = {}
    l = list()

    def __init__(self):
        self.providers['airtel'] = ['9900', '9800', '9811']
        self.providers['BSNL'] = ['9440', '9822']
        self.providers['Idea'] = ['9848', '9912']
        self.providers['Reliance'] = ['9300', '9812']
        obj = JSONReader()
        self.l = obj.get_all()



    def get_filter(self, field, value):
        for i in range(len(self.l)):
            method = ''
            if field == 'emailid':
                method = self.l[i].get_email_id()
            elif field == 'name':
                method = self.l[i].get_name()
            elif field == 'city':
                method = self.l[i].get_city()
            elif field == 'phonenumber':
                method = self.l[i].get_phone_number()
            if value in method:
                print self.l[i].__dict__
            else:
                print "data doesn't exist"
                return




    def get_provider_name(self, phonenumber):
        string1 = phonenumber[0:4]
        for key in self.providers:
            if string1 in self.providers[key]:
                print key
            else:
                print 'others'
                return




    def get_records_of_provider(self, provider):
        list2 = self.providers[provider]
        list3 = []
        for i in range(len(self.l)):
            string2 = self.l[i].get_phone_number()
            phonenumber = string2[0:4]
            if phonenumber in list2:
                list3.append(self.l[i].__dict__)

        if not list3:
            print "data doesn't exist"
            return
        print list3



if __name__ == '__main__':
    dir = Directory()
    dir.get_filter('name', 'hi')

