import psycopg2
from config import config


def update_name(user_id, phone_number):
    
    sql = """
    UPDATE phone_book
    SET phone_number = %s
    WHERE user_id = %s;
    """
    
    conn = None
    update_rows = 0
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phone_number, user_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
      
user_id = int(input())
phone_number = input()   

update_name(user_id, phone_number)