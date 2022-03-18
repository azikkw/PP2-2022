#Palindrom or not

def Palindrom(s):
    t = s[::-1]
    if s == t:
        print("True")
    else:
        print("False")
    
s = input()

Palindrom(s)