
import psycopg2
from config import config

"""
create or replace procedure new_phones(
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

def add_new_phones(users_list):
    
    conn = None
    
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany('call new_phones(%s, %s, %s)', users_list)
        cur.close()
        conn.commit()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()


users_list = [
    ('User7', 'S7', '+79058722166'),
    ('User8', 'S8', '+70958762435'),
    ('User9', 'S9', '+77071583831')
]

        
cnt = 0
for user in users_list:
    file1 = open('first_name.txt', 'r')
    first_list = [line.strip() for line in file1]
    for user_name in first_list:
        if user[0] == user_name:
            cnt += 1
            
    file2 = open('last_name.txt', 'r')
    last_list = [line.strip() for line in file2]
    for user_name in last_list:
        if user[1] == user_name:
            cnt += 1
            
if cnt >= 2:
    print("Error! Among the entered users there are already registered!")
else:
    for user in users_list:
        with open('first_name.txt', 'a') as f:
            f.write(f'{user[0]}\n')
        with open('last_name.txt', 'a') as f:
            f.write(f'{user[1]}\n')
    
    add_new_phones(users_list)
        