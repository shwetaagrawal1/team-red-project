import sys
from contact_app import JSONWriter
from json_reader import JSONReader
from Person import Person
from directory import Directory

class Main:
    writer_obj = JSONWriter()
    reader_obj = JSONReader()
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
            writer_obj.add_contact(person)

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

            writer_obj.modify_contact(person)

        elif case == 3:
            data = reader_obj.get_all()
            try:
                for i in data:
                    print(i.__dict__)
            except:
                print()

        elif case == 4:
            print "Enter number for delete contact:"
            number = input()
            writer_obj.delete_contact(number)

        elif case == 5:
            print "Enter field"
            field = raw_input()
            print "Enter value"
            value = raw_input()
            dir_obj.get_filter(field,value)

        elif case == 6:
            print "Enter Phone number"
            number = raw_input()
            data = reader_obj.get_contacts(number)
            try:
                print(data.__dict__)
            except:
                print()

        elif case == 7:
            print "Enter field"
            field = raw_input()
            print "Enter value"
            value = raw_input()
            p2 = reader_obj.get_field(field, value)
            try:
                for i in p2:
                    print(i.__dict__)
            except:
                print()

        elif case == 8:
            print "Enter Phone number"
            number = raw_input()
            dir_obj.get_provider_name(number)

        elif case == 9:
            print "Enter provider name"
            provider = raw_input()
            dir_obj.get_records_of_provider(provider)

        elif case == 10:
            sys.exit()


if __name__=="__main__":
    Main()