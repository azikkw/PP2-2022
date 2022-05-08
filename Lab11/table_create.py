import psycopg2
from config import config 


def create_table():
    
    command = (
        """
        CREATE TABLE phone_book_update (
            user_id serial PRIMARY KEY,
            first_name VARCHAR (50),  
            last_name VARCHAR (50),  
            phone_number VARCHAR (14) UNIQUE NOT NULL
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