# import sqlite3
# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
#
# # cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
# #                " title varchar(250) NOT NULL UNIQUE,"
# #                " author varchar(250) NOT NULL,"
# #                " rating FLOAT NOT NULL)")
#
# cursor.execute("INSERT INTO books VALUES(2, 'Harry Potters', 'J. K. Rowling', '9.5')")
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# Create the extension
db = SQLAlchemy()
app = Flask(__name__)


# CREATE DATABASE
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"


# Initialise the app with the extension
db.init_app(app)


# CREATE TABLE
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), unique=True, nullable=False)
    rating = db.Column(db.FLOAT, nullable=False)

# Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()


# CREATE RECORD
with app.app_context():
    new_book = Books(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
