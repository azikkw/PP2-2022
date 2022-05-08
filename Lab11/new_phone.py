#Create procedure to insert new user by name and phone, update phone if user already exists

import psycopg2
from config import config

"""
create or replace procedure new_phone(
    first_name varchar,
    last_name varchar,
    phone_number varchar
)
as $$
begin
    INSERT INTO phone_book_update(first_name, last_name, phone_number)
    VALUES(first_name, last_name, phone_number);
end;
$$

language plpgsql;
"""

def add_new_phone(first_name, last_name, phone_number):
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call new_phone(%s, %s, %s)', (first_name, last_name, phone_number))
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()    
            
def update_phone(first_name, last_name, phone_number):
    
    sql = """
    UPDATE phone_book_update
    SET phone_number = %s
    WHERE first_name = %s AND last_name = %s
    """
    
    conn = None
    update_rows = 0
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (phone_number, first_name, last_name))
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
            
first_name = input()
last_name = input()
phone_number = input()

cnt = 0
file1 = open('first_name.txt', 'r')
first_list = [line.strip() for line in file1]
for user in first_list:
    if first_name == user:
        cnt += 1
file2 = open('last_name.txt', 'r')
last_list = [line.strip() for line in file2]
for user in last_list:
    if last_name == user:
        cnt += 1

if cnt != 2:
    with open('first_name.txt', 'a') as f:
        f.write(f'{first_name}\n')
    with open('last_name.txt', 'a') as f:
        f.write(f'{last_name}\n')
    add_new_phone(first_name, last_name, phone_number)
elif cnt :
    print("This user is already registered, change your phone number if it's you")
    global new_phone
    new_phone = input()
    update_phone(first_name, last_name, new_phone)