#Problem I

n = int(input())
a = []

for i in range(n):
    a = str(input())
    if a.find("@gmail.com") != -1:
        print(a.replace("@gmail.com", ""))