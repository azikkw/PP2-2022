# Function that returns all records based on a pattern (example of pattern: part of name, surname, phone number)

import psycopg2
from config import config

"""
create or replace function get_phones()
returns TABLE(user_id integer, first_name varchar, last_name varchar, phone_number varchar) as
$$
begin
    return query
    select phone_book_update.user_id, phone_book_update.first_name, phone_book_update.last_name, phone_book_update.phone_number from phone_book_update;
end;
$$

language plpgsql;
"""

def get_all_phones():
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('get_phones')
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
            
get_all_phones()