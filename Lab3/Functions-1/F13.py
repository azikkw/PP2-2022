#Find the random nubmer in range from 1 to 20

import random

def random_number(a, cnt):
    
    print("Hello! What is your name?")
    s = input()

    for i in a:
        k = random.randrange(0, a[-1])
        t = int(input())
        
        if t == k:
            cnt += 1
            print("Good job,", s, "You guessed my number in", cnt, "guesses!")
            break
        else:
            cnt += 1
            print("Your guess is too low. Take a guess.")
        

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
cnt = 0

random_number(a, cnt)