#Reverse String

def string_reverse(s, t):
    print(" ".join(t[::-1]))
    
s = input()
t = s.split()

string_reverse(s, t)