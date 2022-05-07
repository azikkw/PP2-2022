import psycopg2
from config import config 


def create_table():
    
    command = (
        """
        CREATE TABLE phone_book (
            user_id serial PRIMARY KEY,
            user_name VARCHAR (50) UNIQUE NOT NULL,  
            phone_number VARCHAR (20) UNIQUE NOT NULL
        );
        """
    )
    
    conn = None 
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
    
    
create_table()