from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z]).{8,32}$')
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password_hash = data['password_hash']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f'<User: {self.first_name} {self.last_name}> Object ID: {self.id}'

    @staticmethod
    def validate_user_register(users):
        is_valid = True
        if not users['first_name'] or len(users['first_name']) < 2:
            is_valid = False
        if not users['last_name'] or len(users['last_name']) < 2:
            is_valid = False
        if not users['email'] or not EMAIL_REGEX.match(users['email']):
            flash('Invalid email address!')
            is_valid = False
        if User.get_by_email(users):
            flash('Email already in use.')
            is_valid = False
        if not users['password'] or not PASSWORD_REGEX.match(users['password']):
            flash('Invalid password!')
            is_valid = False
        if users['password'] != users['confirm_password']:
            flash('Passwords do not match!')
            is_valid = False

        return is_valid

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password_hash) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('login-and-registration').query_db(query, data)
    
    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s;"
        result = connectToMySQL('login-and-registration').query_db(query, data)
        print(result)
        if not result:
            return False
        user = cls(result[0])
        print('user found')
        return user

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL('login-and-registration').query_db(query, data)
        user = cls(result[0])
        print('user found')
        return user