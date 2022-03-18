#Function that accepts a string and calculate the number of upper case letters and lower case letters

def count(s, cnt1, cnt2):
    for count in s:
        if count >= 'A' and count <= 'Z':
            cnt1 += 1
        elif count >= 'a' and count <= 'z':
            cnt2 += 1
            
    print('Upper case letters', cnt1)
    print('Lower case letters', cnt2)
    

s = 'JavaScript'
cnt1, cnt2 = 0, 0

count(s, cnt1, cnt2)