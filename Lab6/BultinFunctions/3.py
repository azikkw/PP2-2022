#Function that checks whether a passed string is palindrome or not

def isPalindrome(s1):
    s2 = (s1[::-1])
    
    if s1 == s2:
        print('Yes, it is Palindrome')
    else:
        print('No, it is not Palindrome')
    
    
s1 = input()
isPalindrome(s1)