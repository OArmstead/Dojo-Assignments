# from tkinter.tix import Select
from login_and_register.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask_bcrypt import Bcrypt


class Registration:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO registration_schema.registration (first_name,last_name,email,password) VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)"
        return connectToMySQL('registration_schema').query_db(query,data)


    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM registration_schema.registration;'
        results = connectToMySQL('registration_schema').query_db(query)
        print(results)
        registrations = []
        for r in results:
            registrations.append(cls(r))
        return registrations

    @classmethod
    def get_by_email(cls,data):
        query = 'SELECT * FROM registration WHERE email = %(email)s;'
        result = connectToMySQL('registration_schema').query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])

    @staticmethod
    def validate_registration(registration):
        is_valid = True
        if not EMAIL_REGEX.match(registration['email']):
            flash('Invalid email address!')
            is_valid = False
        is_valid = True

        if len(registration['first_name']) < 3:
            flash('Your first name must be at least 3 characters.')
            is_valid = False
        if len(registration['last_name']) < 3:
            flash('Your last name must have at least 3 characters')
            is_valid = False
        if len(registration['email']) <3:
            flash('Enter a valid email')
            is_valid = False
        if len(registration['password']) < 3:
            flash('Password must be at least 3 characters')
            is_valid = False
        if registration['password'] != registration['confirm_password']:
            flash('Your passwords does not match')
        return is_valid
