from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
import re # the regex module 
# create a regular expression object that we'll use later 
bcrypt = Bcrypt(app) # we are creating an object called bcrypt, which is made by invoking the function Bcrypt with our app arguments
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    DB = "just_users_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = """
                    SELECT * from users 
                """
        results = connectToMySQL(cls.DB).query_db(query)

        all_users = []
        for one_user in results:
            all_users.append(cls(one_user))
        return all_users
    
    @classmethod
    def create_new(cls, data):
        query = """
                    INSERT into users (first_name, last_name, email, password)
                    VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results 

    @classmethod 
    def get_one(cls, user_id):
        query = """
                    SELECT * from users 
                    WHERE id=%(id)s
                """
        data = {"id": user_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0]) 

    @classmethod
    def edit(cls, user_id, user_data):
        data = {
            "id": user_id,
            "first_name": user_data["first_name"],
            "last_name": user_data["last_name"],
            "email": user_data["email"]
        }
        query = """
                    UPDATE users 
                    SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s
                    WHERE id=%(id)s
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, user_id):
        data = {"id": user_id}
        query = "DELETE from users WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True  
        if len(user["first_name"]) < 2:
            flash("First name must be at least 2 characters.")
            is_valid = False 
        if len(user["last_name"]) < 2:
            flash("Last name must be at least 2 characters.")
            is_valid = False 
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']):
            flash("Email address is invalid.")
            is_valid = False

        all_emails = []
        all_users = User.get_all()
        for one_user in all_users:
            all_emails.append(one_user.email)

        if user['email'] in all_emails:
            flash("Email is associated with an existing user.")
            is_valid = False

        return is_valid

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        # didn't find a matching user 
        if len(result) < 1:
            return False 
        return cls(result[0])

