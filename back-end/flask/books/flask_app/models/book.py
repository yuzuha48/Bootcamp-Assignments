from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    DB = "books_schema"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []

    @classmethod
    def save(cls, book_data):
        data = {
                "title": book_data["title"],
                "num_of_pages": book_data["num_of_pages"]
            }
        query = """
                    INSERT INTO books (title, num_of_pages, created_at, updated_at)
                    VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result 

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        result = connectToMySQL(cls.DB).query_db(query)
        return result

    @classmethod
    def get_one(cls, book_id):
        data = {"id": book_id}
        query = "SELECT * FROM books WHERE id=%(id)s;"
        result = connectToMySQL(cls.DB).query_db(query, data)
        book = cls(result[0])
        return book

    @classmethod
    def get_favorited_by(cls, book_id):
        data = {"id": book_id}
        query = """
                    SELECT * FROM books
                    LEFT JOIN favorites 
                    ON favorites.book_id = books.id
                    LEFT JOIN authors 
                    ON favorites.author_id = authors.id
                    WHERE books.id = %(id)s;
                """
        results = connectToMySQL(cls.DB).query_db(query, data)
        book = cls(results[0])

        for row_in_db in results:
            author_data = {
                "id": row_in_db["authors.id"],
                "name": row_in_db["name"],
                "created_at": row_in_db["authors.created_at"],
                "updated_at": row_in_db["authors.updated_at"]
            }
            book.authors.append(author.Author(author_data))

        return book

    @classmethod
    def add_author(cls, book_id, author_id):
        data = {
        "author_id": author_id,
        "book_id": book_id
        }
        query = """
                    INSERT INTO favorites (author_id, book_id)
                    VALUES (%(author_id)s, %(book_id)s);
                """
        connectToMySQL(cls.DB).query_db(query, data)
        book = Book.get_one(book_id)
        book.authors.append(author.Author.get_one(author_id))
        return book

    @classmethod
    def get_unfavorited_books(cls, author_id):
        data = {"id": author_id}
        query = """
                    SELECT * FROM books 
                    WHERE books.id NOT IN 
                    (SELECT book_id from favorites WHERE author_id = %(id)s);
                """
        result = connectToMySQL(cls.DB).query_db(query, data)
        books = []
        for row in result:
            books.append(cls(row))
        return books 