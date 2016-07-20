from os import abort
from flask import Flask, render_template, request, url_for, redirect, jsonify, json
from Person import Person
from directory import Directory



app = Flask(__name__)
dir_obj = Directory()
person = Person()


@app.route('/create_contact', methods=['POST'])
def create_contact():
    task = request.json
    print task
    person.set_name(task["name"])
    person.set_phone_number(task["number"])
    person.set_email_id(task["email"])
    person.set_city(task["city"])
    statement = dir_obj.add_contact_directory(person)
    return statement, 201


@app.route('/modify_contact', methods=['POST'])
def modify_contact():
    task = request.json
    try:
        person.set_name(task["name"])
    except:
        print " "
    try:
        person.set_phone_number(task["number"])
    except:
        return "phone number is not present to modify", 201
    try:
        person.set_email_id(task["email"])
    except:
        print ""
    try:
        person.set_city(task["city"])
    except:
        print ""
    dir_obj.modify_contact_directory(person)
    return "modified", 201


@app.route('/get_directory', methods=['GET'])
def get_directory():
    data = dir_obj.get_all_directory()
    tasks = []
    try:
        for index_data in data:
            tasks.append(index_data.__dict__)
        return jsonify({'data': tasks}),201
    except:
        print data


@app.route('/delete_number/<number>', methods=['GET'])
def delete_number(number):
    try:
        dir_obj.delete_contact_directory(number)
        return "number is deleted", 201
    except:
        return  "number doesn't exist in database",201


@app.route('/get_filter/<fieldvalue>', methods=['GET'])
def get_filter(fieldvalue):
    field = fieldvalue.split("=")[0]
    value = fieldvalue.split("=")[1]
    list_records = dir_obj.get_filter(field, value)
    if not list_records:
        return "data doesn't exist",201
    else:
        for records in list_records:
            return jsonify({'data':records.__dict__}),201


@app.route('/get_contact_details/<number>', methods=['GET'])
def get_contact_details(number):
    data_records = dir_obj.get_contacts_directory(number)
    tasks = []
    try:
        for data in data_records:
            tasks.append(data.__dict__)
        return jsonify({'data': tasks}), 201
    except:
        return  str(data_records),201


@app.route('/get_field_directory/<fieldvalue>', methods=['GET'])
def get_field_directory(fieldvalue):
    field = fieldvalue.split("=")[0]
    value = fieldvalue.split("=")[1]
    person_record = dir_obj.get_field_directory(field, value)
    tasks = []
    try:
        for index_data in person_record:
            tasks.append(index_data.__dict__)
        return jsonify({'data': tasks}), 201
    except:
        return str(person_record), 201


@app.route('/get_provider_name/<number>', methods=['GET'])
def get_provider_name(number):
    name = dir_obj.get_provider_name(number)
    return name, 201



@app.route('/get_records_of_provider/<provider>', methods=['GET'])
def get_records_of_provider(provider):
    list_provider = dir_obj.get_records_of_provider(provider)
    tasks = []
    if not list_provider:
        return "data doesn't exist",201
    else:
        for person in list_provider:
            tasks.append(person.__dict__)
        return jsonify({'data': tasks}), 201




if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)