from json_reader import JSONReader
from contact_app import JSONWriter

class Directory:
    providers = {}
    temp_list = []
    l_data = list()
    method = ""

    def __init__(self):
        self.providers['airtel'] = ['9900', '9800', '9811']
        self.providers['BSNL'] = ['9440', '9822']
        self.providers['Idea'] = ['9848', '9912']
        self.providers['Reliance'] = ['9300', '9812']
        self.method = ""
        self.reader_obj = JSONReader()
        self.writer_obj = JSONWriter()
        self.l_data = list()



    def get_filter(self, field, value):
        self.l_data = list()
        self.l_data = self.reader_obj.get_all()
        for records in self.l_data:
            if field == 'emailid':
                self.method = records.get_email_id()
            elif field == 'name':
                self.method = records.get_name()
            elif field == 'city':
                self.method = records.get_city()
            elif field == 'phonenumber':
                self.method = records.get_phone_number()
            if value in self.method:
                self.temp_list.append(records)
        return self.temp_list




    def get_provider_name(self, phonenumber):
        self.l_data = list()
        self.l_data = self.reader_obj.get_all()
        string1 = phonenumber[0:4]
        for index_provider in self.providers:
            provider_name_list =  self.providers[index_provider]
            if string1 in provider_name_list:
                return index_provider
        return "others"

    def get_records_of_provider(self, provider):
        self.l_data = list()
        self.l_data = self.reader_obj.get_all()
        list2 = self.providers[provider]
        list3 = []
        for index in range(len(self.l_data)):
            string2 = self.l_data[index].get_phone_number()
            string2 = string2[0:4]
            if string2 in list2:
                list3.append(self.l[index].__dict__)

        return list3

    def add_contact_directory(self,person):
        return self.writer_obj.add_contact(person)

    def modify_contact_directory(self, person):
        self.writer_obj.modify_contact(person)

    def delete_contact_directory(self, number):
        self.writer_obj.delete_contact(number)

    def get_all_directory(self):
        return self.reader_obj.get_all()

    def get_contacts_directory(self,number):
        data =  self.reader_obj.get_contacts(number)
        return data

    def get_field_directory(self,field, value):
        return self.reader_obj.get_field(field, value)



if __name__ == '__main__':
    dir = Directory()
    person = dir.get_records_of_provider("airtel")
    if not person:
        print "data doesn't exist"
    else:
        for p in person:
            print p.__dict__
