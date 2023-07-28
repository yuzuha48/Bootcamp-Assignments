from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Cookie():
    DB = "cookies"
    def __init__(self, data):
        self.id = data["id"]
        self.customer_name = data["customer_name"]
        self.cookie_type = data["cookie_type"] 
        self.num_of_boxes = data["num_of_boxes"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies;"
        results = connectToMySQL(cls.DB).query_db(query)

        all_orders = []
        for one_row in results:
            all_orders.append(cls(one_row))
        return all_orders

    @classmethod
    def save(cls, cookie_data):
        data = {
            "customer_name": cookie_data["customer_name"],
            "cookie_type": cookie_data["cookie_type"],
            "num_of_boxes": cookie_data["num_of_boxes"]
        }
        query = "INSERT INTO cookies (customer_name, cookie_type, num_of_boxes) VALUES (%(customer_name)s, %(cookie_type)s, %(num_of_boxes)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_one(cls, cookie_id):
        data = {"id": cookie_id}
        query = "SELECT * FROM cookies WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def edit(cls, cookie_id, cookie_data):
        data = {
            "id": cookie_id,
            "customer_name": cookie_data["customer_name"], 
            "cookie_type": cookie_data["cookie_type"],
            "num_of_boxes": cookie_data["num_of_boxes"]
            }
        query = """
                UPDATE cookies 
                SET customer_name=%(customer_name)s, cookie_type=%(cookie_type)s, num_of_boxes=%(num_of_boxes)s 
                WHERE id=%(id)s;
                """
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_order(cookie_order):
        is_valid = True
        if len(cookie_order["customer_name"]) < 2:
            flash("Customer name must be at least 2 characters.")
            is_valid = False
        if len(cookie_order["cookie_type"]) < 2:
            flash("Cookie type must be at least 2 characters.")
            is_valid = False
        if cookie_order["num_of_boxes"] == "" or int(cookie_order["num_of_boxes"]) < 1:
            flash("Number of boxes must be at least 1.")
            is_valid = False

        return is_valid



