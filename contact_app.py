import json
from json_reader import JSONReader

class JSONWriter:
    def __init__(self):
        self.temp_dict = {}
        get_obj = JSONReader()
        data = get_obj.get_all()
        if data != ['none']:
            for recordes in data:
                self.temp_dict.update({recordes.get_phone_number(): {"name": recordes.get_name(), "email": recordes.get_email_id(),"city": recordes.get_city()}})

    def add_contact(self,person):

        dict = {person.get_phone_number():{"name":person.get_name(),"email":person.get_email_id(),"city":person.get_city()}}
        if person.get_phone_number() in self.temp_dict.keys():
            return "contact is exixt"
        self.temp_dict.update(dict)

        with open("jsonFile.json", "w") as filepointer:
            json.dump(self.temp_dict,filepointer, indent=2)



        """ with open("jsonFile.json","r") as filepointer:
            if filepointer.read() == "":
                with open("jsonFile.json", "w") as filepointer:
                    json.dump(dict, filepointer)
            else:
                filepointer.seek(0)
                data = json.load(filepointer)
                if str(person.get_phone_number()) in data.keys():
                    print("person already exist")
                else:
                    data.update(dict)
                    with open("jsonFile.json", "w") as filepointer:
                        filepointer.write(json.dumps(data))"""

    def delete_contact(self,number):

        if number in self.temp_dict.keys():
            del self.temp_dict[number]
        with open("jsonFile.json", "w") as filepointer:
            json.dump(self.temp_dict, filepointer, indent=2)
        return "contact deleted successfully"


    """ with open("jsonFile.json", "r") as filepointer:
            if filepointer.read() == "":
                print "Directory is empty"
            else:
                filepointer.seek(0)
                data = filepointer.read()
                data = eval(data)
                if str(number) in data.keys():
                    del data[str(number)]
                    print "number deleted successfully"
                    with open("jsonFile.json", "w") as filepointer:
                        filepointer.write(json.dumps(data))

                else:
                    print "number not exist" """

    def modify_contact(self, person):
        if person.get_phone_number() in self.temp_dict.keys():
            x = self.temp_dict[person.get_phone_number()]
            if (len(person.get_name()) != 0):
                x["name"] = person.get_name()
            if (len(person.get_city()) != 0):
                x["city"] = person.get_city()
            if (len(person.get_email_id()) != 0):
                x["email"] = person.get_email_id()
            y = {person.get_phone_number(): x}
            self.temp_dict.update(y)
            with open("jsonFile.json", "w") as filepointer:
                json.dump(self.temp_dict, filepointer, indent=2)
            return "contact updataed successfully"

        """with open("jsonFile.json", "r") as filepointer:
            if filepointer.read() == "":
                print "Directory is empty"
            else:
                filepointer.seek(0)
                data = filepointer.read()
                data = eval(data)
                if person.get_phone_number() in data.keys():
                    x = data[person.get_phone_number()]
                    if (len(person.get_name()) != 0):
                        x["name"] = person.get_name()
                    if (len(person.get_city()) != 0):
                        x["city"] = person.get_city()
                    if (len(person.get_email_id()) != 0):
                        x["email"] = person.get_email_id()
                    y = {person.get_phone_number(): x}
                    data.update(y)
                    print "number updated successfully"
                    with open("jsonFile.json", "w") as filepointer:
                        filepointer.write(json.dumps(data))

                else:
                    print "number not exist"""""

