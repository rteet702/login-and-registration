from flask_app.config.mysqlconnection import connectToMySQL


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
    def validate_user(users):
        is_valid = True
        if not users['first_name'] or len(users['first_name']) < 2:
            is_valid = False
        if not users['last_name'] or len(users['last-name']) < 2:
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
        user = cls(result[0])
        print('user found')
        return user