import psycopg2
from config import config 


def create_table():
    
    command = (
        """
        CREATE TABLE snake_results (
            user_id serial PRIMARY KEY,
            user_name VARCHAR (50),
            user_level VARCHAR (20),
            user_score VARCHAR (20)
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