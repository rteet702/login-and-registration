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

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password_hash) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL('login-and-registration').query_db(query, data)