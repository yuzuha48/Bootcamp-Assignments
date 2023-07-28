from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user 
from flask_app.models import post
import datetime

class Comment:
    DB = "login_and_registration"
    def __init__(self, data):
        self.id = data['id']
        self.comment_text = data['comment_text']
        self.created_at = data['created_at'].strftime("%B %d, %Y")
        self.updated_at = data['updated_at'].strftime("%B %d, %Y")
        self.user = None 
        self.post = None 

    @classmethod
    def save_comment(cls, user_id, post_id, comment_data):
        data = {
            "comment_text": comment_data["comment_text"],
            "users_id": user_id,
            "posts_id": post_id
        }
        query = """
                INSERT into comments (comment_text, users_id, posts_id) 
                VALUES (%(comment_text)s, %(users_id)s, %(posts_id)s);
                """

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """
                SELECT * FROM comments 
                JOIN posts ON posts.id = comments.posts_id
                JOIN users ON users.id = comments.users_id
                """
        result = connectToMySQL(cls.DB).query_db(query)
        all_comments = []
        for row in result:
            one_comment = cls(row)
            user_data = {
                "id": row["users.id"],
                "first_name": row["first_name"], 
                "last_name": row["last_name"],
                "email": row["email"],
                "password": row["password"],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            one_comment.user = user.User(user_data)

            post_data = {
                "id": row['posts.id'], 
                "content": row['content'],
                "created_at": row['posts.created_at'],
                "updated_at": row['posts.updated_at']
            }
            one_comment.post = post.Post(post_data)

            all_comments.append(one_comment)

        return all_comments

    @classmethod
    def delete_comments_with_post(cls, post_id):
        data = {"posts_id": post_id}
        query = "DELETE FROM comments WHERE posts_id=%(posts_id)s;"
        return connectToMySQL(cls.DB).query_db(query, data)
