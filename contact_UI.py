from flask import Flask
from flask import request
from Person import Person
from flask import render_template
from directory import Directory

app = Flask(__name__)
dir_obj = Directory()
person = Person()
@app.route('/')
def my_form():
    return render_template("home.html")

@app.route('/add_contacts')
def addcontact():
    return render_template("add_contact.html")
@app.route('/add_contacts_method', methods =['GET'])
def addcontctsmethod():
    name = request.args['name']
    person.set_name(name)
    number = request.args["number"]
    person.set_phone_number(number)
    email = request.args["email"]
    person.set_email_id(email)
    city = request.args["city"]
    person.set_city(city)
    statement = dir_obj.add_contact_directory(person)
    if statement == None:
        statement = "Contact added successfully"

    return render_template("add_contact.html", result=statement)

@app.route('/modify_contacts')
def modifycontact():
    return render_template("/modify_contacts.html")
@app.route('/modify_contacts_method', methods =['GET'])
def modifycontctsmethod():
    name = request.args['name']
    person.set_name(name)
    number = request.args["number"]
    person.set_phone_number(number)
    email = request.args["email"]
    person.set_email_id(email)
    city = request.args["city"]
    person.set_city(city)
    statement = dir_obj.modify_contact_directory(person)

    return render_template("addcontact_statement.html", result=statement)

@app.route('/delete_contacts')
def deletecontact():
    return render_template("delete_contacts.html")
@app.route('/delete_contacts_method', methods =['GET'])
def deletecontctsmethod():
    number = request.args["number"]
    person.set_phone_number(number)
    statement = dir_obj.delete_contact_directory(number)

    return render_template("addcontact_statement.html", result=statement)

@app.route('/display_contacts')
def displaycontact():
    statement = dir_obj.get_all_directory()
    return render_template("display_contacts.html", result = statement)

@app.route('/filter_by_fields')
def filtercontact():
    return render_template("filter_by_fields.html")
@app.route('/filter_by_fields_method', methods =['GET'])
def filtercontctsmethod():
    field = request.args["field"]
    value = request.args["value"]
    statement = dir_obj.get_filter(field,value)


    return render_template("filter_by_field_statement.html", result=statement)


@app.route('/contact_by_numbers')
def contactsbynumber():
    return render_template("contacts_by_number.html")
@app.route('/contacts_by_number_method', methods =['GET'])
def contactsbynumbermethod():
    phone_number= request.args["number"]
    statement = dir_obj.get_contacts_directory(phone_number)
    print statement
    return render_template("contact_by_number_statement.html", result=statement)


@app.route('/contacts_by_field')
def contactsbyfield():
    return render_template("contacts_by_field.html")
@app.route('/contacts_by_field_method', methods =['GET'])
def contactsbyfieldmethod():
    field = request.args["field"]
    value = request.args["value"]
    statement = dir_obj.get_field_directory(field, value)


    return render_template("contacts_by_field_statement.html", result=statement)
@app.route('/providers_name')
def providersname():
    return render_template("providers_name.html")
@app.route('/providers_name_method',methods=['GET'])
def providersnamemethod():
    phone_number=request.args["number"]
    statement=dir_obj.get_provider_name(phone_number)
    return render_template("providers_name_statement.html",result=statement)


@app.route('/display_contact_by_providers')
def providersname1():
    return render_template("providers_number.html")
@app.route('/numbers_by_providers_name',methods=['GET'])
def providersnamecontacts():
    provider = request.args["provider"]
    statement= dir_obj.get_records_of_provider(provider)
    print statement
    return render_template("records_of_providers.html",result=statement)

if __name__ == '__main__':
    app.run()