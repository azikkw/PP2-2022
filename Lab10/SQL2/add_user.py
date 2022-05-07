import psycopg2
from config import config


def add_user(user_name, user_level, user_score):
    
    sql = """
    INSERT INTO snake_results(user_name, user_level, user_score)
    VALUES(%s, %s, %s) RETURNING user_id;
    """
    
    conn = None
    user_id = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (user_name, user_level, user_score))
        user_id = cur.fetchone()[0]
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()     