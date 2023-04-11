from flask_sqlalchemy import SQLAlchemy
#from dao.genre import Genre
#from dao.song import Song

'''
SQLAlchemy is a Python library for working with SQL databases. 
It provides an ORM (Object-Relational Mapping) that allows you to define database tables and 
queries using Python classes and methods.

With SQLAlchemy, you can interact with a database using Python code without having to write
any SQL queries directly. SQLAlchemy supports multiple database backends, including SQLite, 
MySQL, and PostgreSQL.

Some of the features of SQLAlchemy include:
- A simple and intuitive API
- Powerful query generation and manipulation
- Automatic handling of SQL transactions
- Support for advanced SQL features like subqueries, joins, and unions
- Support for multiple database backends
- Compatibility with popular Python web frameworks like Flask and Django

Overall, SQLAlchemy is a powerful tool for working with SQL databases in Python, 
and its ORM makes it easy to interact with databases in a more Pythonic way.
'''

# Esto es el ORM, SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()