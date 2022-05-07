import psycopg2
from config import config


def show_score(user_name):
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM snake_results WHERE user_name='{user_name}';")
        score = cur.fetchone()
        print(f'ID: {score[0]}\nName: {score[1]}\nLevel: {score[2]}\nScore: {score[3]}\n')
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()