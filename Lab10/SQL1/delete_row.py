import psycopg2
from config import config


def delete_row(id_number):
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM phone_book WHERE user_id={id_number};")
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
      
id_number = int(input())

delete_row(id_number)