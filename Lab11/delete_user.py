from delete_user_function import delete_id, delete_name, delete_phone

print(f'Please choose way!\n1. By ID\n2. By name\n3. By phone')
way = input()

if way == 'id':
    print('Please, write ID-number')
    id_number = int(input())
    delete_id(id_number)
    print('Successful deletion')
elif way == 'name':
    print('Please, write name')
    first_name = input()
    last_name = input()
    delete_name(first_name, last_name)
    print('Successful deletion')
elif way == 'phone':
    print('Please, write phone number')
    phone_number = input()
    delete_phone(phone_number)
    print('Successful deletion')