import sqlite3
db = sqlite3.connect("books-collection.db")
cursor = db.cursor()

# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY,"
#                " title varchar(250) NOT NULL UNIQUE,"
#                " author varchar(250) NOT NULL,"
#                " rating FLOAT NOT NULL)")

cursor.execute("INSERT INTO books VALUES(2, 'Harry Potters', 'J. K. Rowling', '9.5')")
db.commit()

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
