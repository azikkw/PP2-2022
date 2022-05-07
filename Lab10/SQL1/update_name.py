import psycopg2
from config import config


def update_name(user_id, user_name):
    
    sql = """
    UPDATE phone_book
    SET user_name = %s
    WHERE user_id = %s;
    """
    
    conn = None
    update_rows = 0
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name, user_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
      
user_id = int(input())
user_name = input()   

update_name(user_id, user_name)