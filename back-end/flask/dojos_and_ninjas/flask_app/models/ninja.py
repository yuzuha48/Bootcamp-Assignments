from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    DB = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = """
                    INSERT into ninjas (first_name, last_name, age, dojo_id, created_at,updated_at)
                    VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(),NOW());
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def delete(cls, ninja_id):
        data = {"id": ninja_id}
        query = " DELETE from ninjas WHERE id=%(id)s"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def get_one(cls, ninja_id):
        data = {"id": ninja_id}
        query = """
                    SELECT * from ninjas
                    WHERE id=%(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])
    
    @classmethod 
    def update(cls, ninja_id, ninja_data):
        data = {
            "id": ninja_id, 
            "first_name": ninja_data["first_name"],
            "last_name": ninja_data["last_name"], 
            "age": ninja_data["age"]
        }
        query = """
                    UPDATE ninjas
                    SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s
                    WHERE id=%(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results