## 1
```python
from itertools import permutations

a = "346 45 16 12567 24 1347 46".split()
s = "АЖ АБ БЖ БЕ БД ЕД БВ ВД ВГ ДГ".split()

print("1 2 3 4 5 6 7")
for p in permutations("АБВГДЕЖ"):
    if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
        print(*p)
```
## 2
```python
print("x y w z")
for x in 0,1:
    for y in 0,1:
        for w in 0,1:
            for z in 0,1:
                f = (x or (not y)) and (not (x == z)) and (not w)
                if f:
                    print(x, y, w, z)
```
## 5
```python
c  = 0
for n in range(100_000_000, 200_000_001):
    sm = sum(map(int, str(n)))
    b = bin(sm)[2:]
    if b.count("1") % 2 == 0:
        b = "1" + b + "00"
    else:
        b = "10" + b + "1"
    r = int(b, 2)
    if r == 21:
        c += 1
print(c)
```
## 6
```python
from turtle import *

screensize(10000, 10000)
tracer(0)
m = 30

for _ in range(3):
    lt(90)
    for i in range(4):
        fd(5 * m)
        rt(90)



up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, "blue")
update()
exitonclick()
```
## 7
```python
print((967 * 1024 * 1024 * 8) / (4 * 192 * 1000 * 16))
```
## 8
```python
from itertools import *
c = 0
for w in permutations("ГЛУБИНА"):
    w = "".join(w)
    if "ГА" not in w and w.index("Г") < w.index("А"):
        print(w)
        c += 1
print(c)
```
## 9
```python
c = 0
for line in open("tmp.txt"):
    a = [int(i) for i in line.split()]
    p = [i for i in a if a.count(i) == 2]
    np = [i for i in a if a.count(i) == 1]
    m = max(a)
    if len(p) == 2 and len(np) == 4 and (max(a) + min(a)) / 2 > (sum(a) - max(a) - min(a)) / 4:
        c += 1
print(c)
```
## 12
```python
from fnmatch import fnmatch

def prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5)+1))

for i in range(2273, 10**9, 2273):
    if fnmatch(str(i), "5*35?5*1") and prime(sum(map(int, str(i)))):
        print(i, i // 2273)
```

## 13
```python
from ipaddress import *
c = 0
ans = []
for m in range(33):
    net1 = ip_network(f"161.137.200.35/{m}", 0)
    net2 = ip_network(f"161.137.150.118/{m}", 0)
    if net1.network_address != net2.network_address:
        print(net1.network_address)
```
## 14
```python
for x in range(1, 3001):
    n = 7**100 - x
    s = ""
    while n:
        s += str(n % 7)
        n //= 7
    if s.count("0") == 2:
        print(x)
```
## 15
```python
print(min(a for a in range(1000) if all((11 <= y) or (7*y < x) or (a > x*y) for x in range(1000) for y in range(1000))))
```
## 16
```python
from sys import setrecursionlimit
setrecursionlimit(10**7)

def g(n):
    if n < 10:
        return n
    if n >= 10:
        return g(n - 2) + 1


def f(n):
    return g(n - 1)

c = 0
for i in range(1, 101):
    if f(i)**0.5 == int(f(i)**0.5):
        c += 1
        print(f(i))
print(c)
```
## 17
```python
a = [int(i) for i in open("tmp.txt")]
m = min(i for i in a if 10 <= abs(i) <= 99 and i % sum(map(int, str(i))) == 0)

ans = []
for x, y in zip(a, a[1:]):
    if x % m == 0 or y % m == 0:
        ans.append(x+y)
print(len(ans), min(ans))
```
## 19-21
```python
def F(s, n):
    if s == 0: return n % 2 == 0
    if n == 0: return 0
    h = [F(s//3,n-1)]
    if s >= 5:
        h.append(F(s-5, n-1))
    return any(h) if n % 2 != 0 else all(h)


print(f"19. {[s for s in range(1, 100) if F(s, 2)]}")
print(f"20. {[s for s in range(1, 100) if not F(s, 1) and F(s, 3)]}")
print(f"21. {[s for s in range(1, 100) if not F(s, 2) and F(s, 4)]}")
```
## 23
```python
def f(n, end):
    if n > end:
        return 0
    if n == 20:
        return 0
    if n == end:
        return 1
    return f(n+1, end) + f(n+3, end) + f(n**2, end)

print(f(2,15) * f(15, 35))
```
## 24
```python
import re

s = open("tmp.txt").readline()

pat1 = r"(?:[A-Z][0-9])*"
pat2 = r"(?:[0-9][A-Z])*"

print(max(len(c) for c in re.findall(pat1, s)))
print(max(len(c) for c in re.findall(pat2, s)))
```
## 25
```python
from fnmatch import fnmatch

for i in range(2273, 10**9, 2273):
    if fnmatch(str(i), "5*35?5*1"):
        print(i, i // 2273)
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

cls = [cl for cl in cls if len(cl) > 20]
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
print(int(px * 10000), int(py * 10000))
```