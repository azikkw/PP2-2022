#Permutation of given string

from itertools import permutations

def Permutation(s):
    t = permutations(s)
    for i in t:
        print("".join(i))


s = input()
Permutation(s)