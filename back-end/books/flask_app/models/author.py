from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    DB = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def save(cls, author_data):
        data = {"name": author_data["name"]}
        query = """
                    INSERT INTO authors (name, created_at, updated_at)
                    VALUES (%(name)s, NOW(), NOW());
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result

    @classmethod
    def get_one(cls, author_id):
        data = {"id": author_id}
        query = "SELECT * FROM authors WHERE id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        author = cls(results[0])
        return author

    @classmethod
    def get_favorite_books(cls, author_id):
        data = {"id": author_id}
        query = """
                    SELECT * FROM authors
                    LEFT JOIN favorites 
                    ON favorites.author_id = authors.id
                    LEFT JOIN books 
                    ON favorites.book_id = books.id
                    WHERE authors.id = %(id)s;
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        author = cls(result[0])

        for row_in_db in result:
            book_data = {
                "id": row_in_db["books.id"],
                "title": row_in_db["title"], 
                "num_of_pages": row_in_db["num_of_pages"],
                "created_at": row_in_db["books.created_at"],
                "updated_at": row_in_db["books.updated_at"]
            }
            author.favorite_books.append(book.Book(book_data))

        return author

    @classmethod
    def add_to_favorites(cls, author_id, book_id):
        data = {
            "author_id": author_id,
            "book_id": book_id
        }
        query = """
                    INSERT INTO favorites (author_id, book_id)
                    VALUES (%(author_id)s, %(book_id)s);
                """
        connectToMySQL(cls.DB).query_db(query, data)
        author = Author.get_one(author_id)
        author.favorite_books.append(book.Book.get_one(book_id))
        return author

    @classmethod
    def get_unfavorited_authors(cls,  book_id):
        data = {"id": book_id}
        query = """ 
                    SELECT * FROM authors 
                    WHERE authors.id NOT IN 
                    (SELECT author_id FROM favorites 
                    WHERE book_id=%(id)s);
                """

        # we get a list of all authors that liked the book, and then we look for all authors that did not like the book (if the author id is not in that initial list, select all)

        result = connectToMySQL(cls.DB).query_db(query, data)

        authors = []
        for row in result:
            authors.append(cls(row))
        return authors

