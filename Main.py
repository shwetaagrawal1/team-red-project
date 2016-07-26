import sys
from Person import Person
from directory import Directory

class Main:

    dir_obj = Directory()
    person = Person()
    while(1):
        print "Enter number 1.ADD CONTACT   2.MODIFY CONTACT    3.DISPLAY CONTACT   4.DELETE CONTACT    5.FILTER BY FIELD  6.CONTACTS BY NUMBER  7.CONTACTS BY FIELD  " \
              "8.DISPLAY PROVIDER NAME  9.DISPLAY CONTACTS BY PROVIDER   10.EXIT"
        case = input()
        if case == 1:
            print "Enter name:"
            name = raw_input()
            person.set_name(name)
            print "Enter contact number:"
            number = raw_input()
            person.set_phone_number(number)
            print "Enter email:"
            email = raw_input()
            person.set_email_id(email)
            print "Enter  city:"
            city = raw_input()
            person.set_city(city)
            statement = dir_obj.add_contact_directory(person)
            if statement != None:
                print statement

        elif case == 2:
            print "Enter contact number for modification:"
            number = raw_input()
            person.set_phone_number(number)
            print "Enter name if u want modify:"
            name = raw_input()
            person.set_name(name)
            print "Enter email if u want modify:"
            email = raw_input()
            person.set_email_id(email)
            print "Enter  city if u want modify:"
            city = raw_input()
            person.set_city(city)

            dir_obj.modify_contact_directory(person)

        elif case == 3:
            data = dir_obj.get_all_directory()
            try:
                for index_data in data:
                    print(index_data.__dict__)
            except:
                print data

        elif case == 4:
            print "Enter number for delete contact:"
            number = raw_input()
            dir_obj.delete_contact_directory(number)

        elif case == 5:
            print "Enter field"
            field = raw_input()
            print "Enter value"
            value = raw_input()
            list_records = dir_obj.get_filter(field,value)
            if not list_records:
                print "data doesn't exist"
            else:
                for records in list_records:
                    print records.__dict__


        elif case == 6:
            print "Enter Phone number"
            number = raw_input()
            data_records = dir_obj.get_contacts_directory(number)
            try:
                for data in data_records:
                    print(data.__dict__)
            except:
                print data_records

        elif case == 7:
            print "Enter field"
            field = raw_input()
            print "Enter value"
            value = raw_input()
            person_record = dir_obj.get_field_directory(field, value)
            try:
                for index_data in person_record:
                    print(index_data.__dict__)
            except:
                print person_record

        elif case == 8:
            print "Enter Phone number"
            number = raw_input()
            name = dir_obj.get_provider_name(number)
            print name

        elif case == 9:
            print "Enter provider name"
            provider = raw_input()
            list_provider = dir_obj.get_records_of_provider(provider)
            if not list_provider:
                print "data doesn't exist"
            else:
                for person in list_provider:
                    print person

        elif case == 10:
            sys.exit()


if __name__=="__main__":
    Main()