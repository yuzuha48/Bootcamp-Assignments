from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user 
from flask import flash

class Recipe:
    DB = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.date_cooked = data["date_cooked"]
        self.length = data["length"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user = None

    @classmethod
    def get_one(cls, recipe_id):
        data = {"id": recipe_id}
        query = """
                SELECT * FROM recipes 
                JOIN users ON users.id = recipes.users_id
                WHERE recipes.id=%(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        one_recipe = cls(results[0])
        for row in results:
            data = {
                "id": row["users.id"],
                "first_name": row["first_name"], 
                "last_name": row["last_name"], 
                "email": row["email"], 
                "password": row["password"], 
                "created_at": row["users.created_at"], 
                "updated_at": row["users.updated_at"]
            }
        one_recipe.user = user.User(data)
        return one_recipe

    @classmethod
    def get_all(cls):
        query = """ SELECT * FROM recipes 
                JOIN users ON users.id = recipes.users_id
                """
        results = connectToMySQL(cls.DB).query_db(query)
        all_recipes = []
        for row in results:
            one_recipe = cls(row)
            user_data = {
                "id": row['users.id'], 
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_recipe.user = user.User(user_data)
            all_recipes.append(one_recipe)
        return all_recipes

    @classmethod
    def save(cls, recipe_data, user_id):
        data = {
            "name": recipe_data["name"], 
            "description": recipe_data['description'], 
            "instructions": recipe_data['instructions'], 
            "date_cooked": recipe_data["date_cooked"],
            "length": recipe_data['length'],
            "users_id": user_id
        }
        query = """
                INSERT INTO recipes (name, description, instructions, date_cooked, length, users_id) 
                VALUES (%(name)s, %(description)s, %(instructions)s, %(date_cooked)s, %(length)s, %(users_id)s);
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_recipe(data):
        is_valid = True 
        if len(data['name']) < 3 or len(data['description']) < 3 or len(data['instructions']) < 3:
            flash("Name, description, and/or instructions must be at least 3 characters.", "create")
            is_valid = False 
        if not data['date_cooked']:
            flash("Please select the date cooked.", "create")
            is_valid = False
        if 'length' not in data:
            flash("Please select whether or not the meal takes less than 30 minutes to cook.", "create")
            is_valid = False
        return is_valid

    @classmethod
    def edit(cls, recipe_id, recipe_data):
        data = {
            "id": recipe_id,
            "name": recipe_data['name'],
            "description": recipe_data['description'],
            "instructions": recipe_data['instructions'], 
            "date_cooked": recipe_data["date_cooked"], 
            "length": recipe_data["length"]
        }
        query = """
                UPDATE recipes
                SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, date_cooked=%(date_cooked)s, length=%(length)s
                WHERE id=%(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def delete(cls, recipe_id):
        data = {"id": recipe_id}
        query = "DELETE FROM recipes WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)