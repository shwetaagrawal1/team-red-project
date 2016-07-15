import json
from Person import Person

class JSONReader(object):
    path = 'jsonFile.json'

    def get_all(self):
        person_details = list()
        with open(self.path) as data_file1:
            data = json.load(data_file1)
            if data == {}:
                person_details.append('json data is empty')
                return person_details

        map1 = data
        for key in map1:
            person = Person()
            person.set_name(str(map1[key]['name']))
            person.set_city(str(map1[key]['city']))
            person.set_email_id(str(map1[key]['email']))
            person.set_phone_number(str(key))
            person_details.append(person)

        return person_details

########################################################################################################################

    def get_contacts(self, number):
        person_details = list()
        with open(self.path) as data_file1:
            data = json.load(data_file1)
            if data == {}:
                person_details.append('json data is empty')
                return person_details

        if number in data.keys():
            map1 = data[number]
            person = Person()
            person.set_name(str(map1['name']))
            person.set_city(str(map1['city']))
            person.set_email_id(str(map1['email']))
            person.set_phone_number(str(number))
            person_details.append(person)
            return person_details
        else:
            person_details.append('data does not exist')
            return person_details

    ########################################################################################################################

    def get_field(self, field, value):
        person_details = list()
        with open(self.path) as data_file1:
            data = json.load(data_file1)
            if data == {}:
                person_details.append('json data is empty')
                return person_details

        map1 = data
        for key in map1:
            if map1[key][field] == value:
                person = Person()
                person.set_name(str(map1[key]['name']))
                person.set_city(str(map1[key]['city']))
                person.set_email_id(str(map1[key]['email']))
                person.set_phone_number(str(key))
                person_details.append(person)

        if not person_details:
            person_details.append('Provided data doesnt exist')
            return person_details

        return person_details

########################################################################################################################

if __name__ == '__main__':
    obj = JSONReader()
    p = obj.get_all()
    try:
        for i in p:
            print i.__dict__

    except:
        print (p)
    p1 = obj.get_contacts('123')
    try:
        for i in p1:
            print i.__dict__
    except:
        print (p1)
    p2 = obj.get_field('name', 'ram')
    try:
        for i in p2:
            print i.__dict__

    except:
       print p2

