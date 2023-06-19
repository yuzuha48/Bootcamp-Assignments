from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask_app.models import comment
from flask import session
import datetime

class Post:
    DB = "login_and_registration"
    def __init__(self, data):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at'].strftime("%B %d, %Y")
        self.updated_at = data['updated_at'].strftime("%B %d, %Y")
        self.creator = None

    @classmethod 
    def save(cls, data):
        data = {
            "content": data["content"],
            "users_id": session["user_id"]
        }
        query = "INSERT INTO posts (content, users_id) VALUES (%(content)s, %(users_id)s);"
        return connectToMySQL(cls.DB).query_db(query, data)

    @staticmethod
    def validate_post(data):
        is_valid = True 
        if len(data['content']) < 1:
            flash("Post content cannot be blank.")
            is_valid = False 
        return is_valid

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM posts 
                JOIN users ON users.id = posts.users_id;
                """ 
        results = connectToMySQL(cls.DB).query_db(query)
        all_posts = []
        for row in results:
            one_post = cls(row)
            one_post_creator_info = {
                "id": row['users.id'], 
                "first_name": row["first_name"],
                "last_name": row['last_name'],
                "email": row["email"],
                "password": row["password"],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_post.creator = user.User(one_post_creator_info)
            all_posts.append(one_post)
        return all_posts

    @classmethod
    def delete(cls, post_id):
        comment.Comment.delete_comments_with_post(post_id)
        data = {"id": post_id}
        query = "DELETE FROM posts WHERE id=%(id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
        

