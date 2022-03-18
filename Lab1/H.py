#Problem H

s = input()
t = input()

if s.count(t) > 1:
    print(s.find(t), s.rfind(t))
else:
    print(s.find(t))