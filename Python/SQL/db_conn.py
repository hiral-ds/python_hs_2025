import mysql.connector
from db_config import db_config

def get_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        print("Connection successful : ", conn)

        return conn
    except mysql.connector.Error as err:
        print("Connection error : ", err)
        return None
    
get_connection()