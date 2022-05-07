import psycopg2
from config import config


def insert_console(user_name, phone_number):
    
    sql = """
    INSERT INTO phone_book(user_name, phone_number)
    VALUES(%s, %s) RETURNING user_id;
    """
    
    conn = None
    user_id = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name, phone_number))
        user_id = cur.fetchone()[0]
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            

user_name = input()
phone_number = input()

insert_console(user_name, phone_number)