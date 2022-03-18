#Return list with unique elements

def return_unique(s):
    n = []
    for i in s:
        if i not in n:
            n.append(i)
    print(" ".join(n))

t = input()
s = t.split()

return_unique(s)