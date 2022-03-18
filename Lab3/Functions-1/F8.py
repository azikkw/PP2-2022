#True if it contains 007 in order

def order(a, n):
    for i in a:
        if i == 0:
            n.append(i)
        if i == 7:
            n.append(i)

    t = sorted(n)

    if n == t:
        print("True")
    else:
        print("False")
        

a = list(map(int, input().split()))
n = []

order(a, n)