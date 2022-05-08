import psycopg2
from config import config


"""
create or replace procedure delete_by_id(
    id integer
)
as $$
begin
    DELETE FROM phone_book_update WHERE phone_book_update.user_id=id;
end;
$$

language plpgsql;
"""
def delete_id(id_number):
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call delete_by_id(%s)', (id_number, ))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()




"""
create or replace procedure delete_by_name(
    f_n integer,
    l_n integer
)
as $$
begin
    DELETE FROM phone_book_update WHERE phone_book_update.first_name='f_n' and phone_book_update.last_name='f_l';
end;
$$

language plpgsql;
"""
def delete_name(first_name, last_name):
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM phone_book_update WHERE first_name='{first_name}' and last_name='{last_name}';")
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()




"""
create or replace procedure delete_by_phone(
    phone varchar
)
as $$
begin
    DELETE FROM phone_book_update WHERE phone_book_update.phone_number='phone';
end;
$$

language plpgsql;
"""
def delete_phone(phone_number):
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM phone_book_update WHERE phone_number='{phone_number}';")
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()