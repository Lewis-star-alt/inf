## 1
```python
from itertools import permutations

a = "4578 367 26 15 148 238 128 1567".split()
s = "АЗ АБ БЖ БЗ ЖЗ БВ ВЖ ЖЕ ЕД ЕГ ДГ ВГ".split()

print("1 2 3 4 5 6 7 8")
for p in permutations("АБВГДЕЖЗ"):
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
                f = (x and y) or (y == z) or w
                if f == 0:
                    print(x, y, w, z)
```
## 5
```python
for n in range(4,100):
    b = bin(n)[2:]
    print(b)
    r = b[:-1] + b[0:2]
    print(r)
    r = int(r[::-1], 2)
    print(r)
    if r == 123 and b[-1] == "0":
        print(n)
        break
```
## 6
```python
from turtle import *

screensize(10000, 10000)
tracer(0)
m = 30
rt(90 * m)
for _ in range(3):
    rt(45)
    fd(10 * m)
    rt(45)

rt(315)
fd(10 * m)

for _ in range(2):
    rt(90)
    fd(10 * m)

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
from math import floor
print(floor((10**6*300)/(1024*768*12)))
```
## 8
```python
from itertools import permutations
c = 0
s = "ГЛУБИНА"
for w in permutations("ГЛУБИНА"):
    if all(w.index(i) != s.index(i) for i in w):
        c += 1
        print(w)
print(c)
```
## 9
```python
c = 0
for line in open("tmp.txt"):
    a = [int(i) for i in line.split()]

    np = [i for i in a if a.count(i) == 1]
    m = max(a)
    if len(np) == 6 and (max(a) + min(a)) / 2 < (sum(a) - max(a) - min(a)) / 4:
        c += 1
print(c)
```
## 12
```python
for n in range(2, 100):
            s = ">" + "0" * 39 + "1" * n + 39 * "2"
            while ">1" in s or ">2" in s or ">0" in s:
                if ">1" in s:
                    s = s.replace(">1", "22>", 1)
                if ">2" in s:
                    s = s.replace(">2", "2>", 1)
                if ">0" in s:
                    s = s.replace(">0", "1>", 1)
            if sum(int(i) for i in s if i != ">") in [i**2 for i in range(20)]:
                print(n)
```

## 13
```python
from ipaddress import *
c = 0
ans = []
for m in range(33):
    net1 = ip_network(f"176.213.225.119/{m}", 0)
    net2 = ip_network(f"176.213.195.58/{m}", 0)
    if net1.network_address != net2.network_address:
        print(net1.network_address)
```
## 14
```python
for x in range(1, 7050):
    n = 5**100 - x
    s = ""
    while n:
        s += str(n % 5)
        n //= 5
    if s.count("0") == 3:
        print(x)
```
## 15
```python
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
```
## 16
```python
from sys import setrecursionlimit
setrecursionlimit(10**7)

def f(n):
    if n == 1:
        return  1
    if n >1:
        return n + f(n-1)
c = 0
for i in range(1, 101):
    if f(2023) // f(i) % 2 == 0:
        c += 1
print(c)
```
## 17
```python
a = [int(i) for i in open("tmp.txt")]
m = [i for i in a if i % 1000 == 151]
s = sum(m) / len(m)
ans = []

for x, y, z in zip(a, a[1:], a[2:]):
    d = [x, y, z]
    cet = sum(1 for i in d if 1000 <= i <= 9999)
    if 1 < cet < 3 and sum(1 for i in d if i % 13 == 0) > sum(1 for i in d if i % 7 == 0) and all(i > s for i in d):
        ans.append(x+y+z)
print(len(ans), min(ans))
```
## 19-21
```python
def F(s, n):
    if s >= 100: return n % 2 == 0
    if n == 0: return 0
    h = [F(s+7, n-1),  F(s*2,n-1)]
    return any(h) if n % 2 != 0 else all(h)


print(f"19. {[s for s in range(1, 100) if F(s, 2)]}")
print(f"20. {[s for s in range(1, 100) if not F(s, 1) and F(s, 3)]}")
print(f"21. {[s for s in range(1, 100) if not F(s, 2) and F(s, 4)]}")
```
## 23
```python
def f(n, end):
    if n < end or n == 33:
        return 0
    if n == end:
        return 1
    return f(n-3, end) + f(n-4, end)

print(f(44,19))
```
## 24
```python
import re

s = open("tmp.txt").readline()

num = r"[1-9ABCDEFGHI][0-9ABCDEFGHI]*"
print(sorted([c for c in re.findall(num, s) if int(c, 19) % 2 == 0], key=lambda x: int(x, 19)))
```
## 25
```python
from fnmatch import fnmatch

def divs(n):
    d = []
    for i in range(2, n+1):
        if n % i == 0 and i % 2 == 0:
            d.append(i)
    return d


for n in range(65000, 1_000_000):
    if fnmatch(str(n), "6*97*5?") and len(divs(n)) >= 4:
        print(n, sum(divs(n)))
        input()
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