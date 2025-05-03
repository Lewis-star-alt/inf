from itertools import *

def f(x):
    P = 1023 <= x <= 2148
    Q = 1362 <= x <= 3898
    R = 1813 <= x <= 2566
    A = a1 <= x <+ a2
    return ((not Q) <= (P or R)) <= ((not A) <= (not Q))

ox = [i/4 for i in range(1022*4, 3898*4+1)]
m = []
for a1, a2 in combinations(ox, 2):
     if all(f(x) for x in ox):
         m.append(a2-a1)
print(min(m))