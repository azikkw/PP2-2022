#Function that returns True if all elements of the tuple are true

def tuple_f(l):
    print(all(l))
    
    
l = tuple(("apple", 10 > 15, 5 == 7, "banana", "cherry", True, False))

tuple_f(l)