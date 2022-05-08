import psycopg2
from config import config
import re


def insert_console(first_name, last_name, phone_number):
    
    sql = """
    INSERT INTO phone_book_update(first_name, last_name, phone_number)
    VALUES(%s, %s, %s) RETURNING user_id;
    """
    
    conn = None
    user_id = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (first_name, last_name, phone_number))
        user_id = cur.fetchone()[0]
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            

first_name = input()
last_name = input()
phone_number = input()

insert_console(first_name, last_name, phone_number)