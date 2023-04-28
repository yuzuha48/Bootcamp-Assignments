from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    DB = "dojos_and_ninjas_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query = """
                    SELECT * FROM dojos;
                """
        results = connectToMySQL(cls.DB).query_db(query)

        all_dojos = []
        for one_dojo in results:
            all_dojos.append(cls(one_dojo))
        return all_dojos
    
    @classmethod 
    def save(cls, data):
        query = """
                    INSERT into dojos (name)
                    VALUES(%(name)s);
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def get_ninjas(cls, dojo_id):
        data = {"id": dojo_id}
        query = """
                    SELECT * from dojos
                    LEFT JOIN ninjas 
                    ON ninjas.dojo_id=dojos.id 
                    WHERE dojos.id=%(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "age" : row_from_db["age"],
                "created_at" : row_from_db["ninjas.created_at"],
                "updated_at" : row_from_db["ninjas.updated_at"]
            }
            dojo.ninjas.append(Ninja(ninja_data))
        return dojo.ninjas

    @classmethod
    def get_one(cls, dojo_id):
        data = {"id": dojo_id}
        query = """
                    SELECT * from dojos
                    WHERE id=%(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

