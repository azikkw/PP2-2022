#Problem F

n = int(input())
a = []

for i in range(n):
    a = int(input())
    if a <= 10:
        print("Go to work!")
    if a > 10 and a <= 25:
        print("You are weak")
    if a > 25 and a <= 45:
        print("Okay, fine")
    if a > 45:
        print("Burn! Burn! Burn Young!")