import psycopg2
from config import config


def update_user(user_id, user_level, user_score):
    
    sql = """
    UPDATE snake_results
    SET user_level = %s, 
        user_score = %s
    WHERE user_id = %s;
    """
    
    conn = None
    update_rows = 0
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_level, user_score, user_id))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
update_user('5', '21', '25')