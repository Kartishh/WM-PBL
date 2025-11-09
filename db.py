import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="kartish",
        password="1234",
        database="price_tracker"
    )