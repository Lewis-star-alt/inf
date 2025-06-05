## 1
```python
from itertools import permutations

a = "346 45 16 12567 24 1347 46".split()
s = "аб ав бв вд вг ве де ег еж гж".split()

print("1 2 3 4 5 6 7")
for p in permutations("абвгдеж"):
    if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
        print(*p)
```
## 2
```python
print("x y w z f")
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = ((x <= y) or (z == x)) and (w <= z)
                if f == 0:
                    print(x, y, w, z, f)
```
## 5
```python
for n in range(1000):
    r = bin(n)[2:]
    if r.count("1") % 2 == 0:
        r = "1" + r + "00"
    else:
        r = "11" + r
    r = int(r, 2)
    if r >= 412:
        print(n)
        break
```
## 6
```python
from turtle import *

screensize(10000, 10000)
tracer(0)
m = 30

for _ in range(2):
    fd(13 * m)
    rt(90)
    fd(20 * m)
    rt(90)

up()
fd(8 * m)
rt(90)
fd(3 * m)
lt(90)
down()

for _ in range(2):
    fd(16 * m)
    rt(90)
    fd(8 * m)
    rt(90)


up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * m, y * m)
        dot(3, "blue")
update()
exitonclick()
```
## 7
```python
print((5 * 2 * 24 * 48 * 1000) / 56000)
```
## 8
```python
from itertools import *

for i, w in enumerate(product(sorted("БЭПН"), repeat=4)):
    i += 1
    w = "".join(w)
    if i % 2 == 0 and w[0] != "П" and w[-1] != "П" and "ЭЭ" not in w:
        print(i, w)
```
## 9
```python
c = 0
for line in open("tmp.txt"):
    a = [int(i) for i in line.split()]
    if len(a) == len(set(a)) and (max(a) + min(a)) / 2 > (sum(a) - min(a) - max(a)) / 4:
        c += 1
print(c)
```
## 12
```python
def prime(n):
    return all(n % d != 0 for d in range(2, int(n**0.5) + 1))

for n in range(1000):
    s = "9" + n * "1" + n * "2"
    while "91" in s or "92" in s:
        if "91" in s:
            s = s.replace("91", "39", 1)
        if "92" in s:
            s = s.replace("92", "59", 1)
    sm = sum(map(int, s))
    if prime(sm) and len(str(sm)) == 3:
        print(n)
```

## 13
```python
from ipaddress import *


for m in range(33):
    net1 = ip_network(f"154.63.206.129/{m}", 0)
    net2 = ip_network(f"154.63.100.75/{m}", 0)
    if net1.network_address != net2.network_address:
        print(net1.netmask)
```
## 14
```python
ans = []
for x in range(57):
    for y in range(57):
        t = 5 * 57**7 + 3 * 57**6 + x * 57**5 + 6 * 57**4 + 6 * 57**3 + y * 57**2 + 3 * 57 + 5
        n = y * 57 + x
        if t % 56 == 0 and n ** 0.5 == int(n ** 0.5):
            if n == 1764:
                print(x * 57 + y)
```
## 15
```python
def f(x):
    P = 106 <= x <= 218
    Q = 132 <= x <= 388
    R = 183 <= x <= 256
    A = a1 <= x <= a2
    return ( not (Q <= (P or R))) <= ((not A) <= (not Q))

r = []
d = [y for x in (106, 218, 132, 388, 183, 256) for y in (x, x + 0.1, x - 0.1)]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            r += [a2 - a1]
print(round(min(r)))
```
## 16
```python
from sys import setrecursionlimit
setrecursionlimit(10**7)

def f(n):
    if n < 3:
        return 3
    if n >= 3:
        return 2 * n + 5 + f(n - 2)


print(f(3027) - f(3023))
```
## 17
```python
a = [int(i) for i in open("tmp.txt")]
arr = [i for i in a if abs(i) % 1000 == 271]
m = sum(arr) / len(arr)

ans = []
for x, y, z in zip(a, a[1:], a[2:]):
    d = [x, y, z]
    cond = sum(1 for i in d if len(str(abs(i))) == 3)
    c11 = [i for i in d if i % 11 == 0]
    c3 = [i for i in d if i % 3 == 0]
    if 1 <= cond <= 2 and len(c11) > len(c3) and all(i > m for i in d):
        ans.append(sum(d))
print(len(ans), min(ans))
```
## 19-21
```python
def F(s1, s2, n):
    if s1 >= 78 or s2 >= 78: return n % 2 == 0
    if n == 0: return 0
    if s1 > s2:
        h = [F(s1+1, s2, n-1), F(s1+2, s2, n-1), F(s1+3, s2, n-1), F(s1, s2*2, n-1)]
    elif s2 > s1:
        h = [F(s1, s2+1, n-1), F(s1, s2+2, n-1), F(s1, s2+3, n-1), F(s1*2, s2, n-1)]
    else:
        h = [F(s1+1, s2, n-1), F(s1+2, s2, n-1), F(s1+3, s2, n-1), F(s1, s2+1, n-1), F(s1, s2+2, n-1), F(s1, s2+3, n-1)]
    return any(h) if n % 2 != 0 else all(h)


print(f"19. {[s1 + s2 for s1 in range(1, 100) for s2 in range(1, 100) if F(s1, s2, 1)]}")
print(f"20. {[s for s in range(1, 78) if not F(25, s, 1) and F(25, s, 3)]}")
print(f"21. {[s for s in range(1, 78) if not F(69, s, 2) and F(69, s, 4)]}")
```
## 23
```python
def f(n, end):
    if n < end:
        return 0
    if n == 19:
        return 0
    if n == end:
        return 1
    return f(n-2, end) + f(n-1, end) + f(n//2, end)

print(f(36,16) * f(16, 15) * f(15, 12))
```
## 24
```python
import re

s = open("tmp.txt").readline()

pat = r"[1-9A-F][0-9A-F]*"

print(max(len(c) for c in re.findall(pat, s)))
```
## 25
```python
from fnmatch import fnmatch

for i in range(1_000_001_268, 10_000_000_000, 2023):
    if fnmatch(str(i), "1*1"):
         if sum(map(int, str(i))) == 68:
            print(i, i // 2023)


```
```python
f = open("tmp.txt")
next(f)

data = [list(map(int, i.split())) for i in f]

data.sort(key=lambda x: x[1])

ans = [data[0]]
for i in data:
    if i[0] >= ans[-1][1]:
        ans.append(i)


for i in data:
    if i[0] >= ans[-2][1] and i[-1] > ans[-1][1]:
        ans[-1] = i
print(len(ans), ans[-1][1])
```

## 27
```python
from math import dist
from turtle import *
from random import *


def centroid(cluster):
    m = []
    for p1 in cluster:
        sm = sum(dist(p1, p2) for p2 in cluster)
        m.append([sm, p1])
    return min(m)[1]


data = []

for line in open("tmp.txt"):
    x, y = map(float, line.replace(",", ".").split())
    data.append([x, y])

cls = []

while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if dist(p, p1) < 1]
        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    cls.append(cl)

print([len(cl) for cl in cls])

tracer(0)
up()
screensize(10_000, 10_000)
for cl in cls:
    color = random(), random(), random()
    for x, y in cl:
        goto(x * 50, y * 50)
        dot(5, color)
update()
exitonclick()

centroids = [centroid(i) for i in cls]

px = sum(x for x, y in centroids) / len(centroids)
py = sum(y for x, y in centroids) / len(centroids)
print(int(px * 100000), int(py * 100000))
```