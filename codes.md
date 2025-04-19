## 1
```python
from itertools import permutations

a = "345 67 156 17 13 237 246".split()
s = "EB EG BG GA AF FD DC FC EC".split()

print("1 2 3 4 5 6 7")
for p in permutations("ABCDEFG"):
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
                f = (z == (not(y))) and ((not(x)) or y) and w
                if f:
                    print(x, y, w, z)
```
## 5
```python
c = 0
for n in range(1000):
    r = bin(n)[2:].zfill(8).replace("0", "*").replace("1", "0").replace("*", "1")
    if int(r, 2) % 5 == 0:
        r = "100" + r[3:]
    else:
        r = "101" + r[3:]
    r = int(r, 2)
    if r == 180:
        c += 1
print(c)
```
## 6
```python
from turtle import *

screensize(10000, 10000)
tracer(0)
m = 30
for _ in range(2):
    fd(16 * m)
    rt(90)
    fd(9 * m)
    rt(90)

up()
fd(5 * m)
rt(90)
fd(11 * m)
rt(90)
down()

for _ in range(2):
    fd(20 * m)
    rt(90)
    fd(8 * m)
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
from math import floor
print(floor((96468992 * 280) / (1024 * 960 * 11)))
```
## 8
```python
from itertools import product

c = 0
for n in product("567", repeat=12):
    if not "55" in n:
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
    if len(p) == 4 and len(np) == 2 and (max(a) + min(a)) / 2 < (sum(a) - max(a) - min(a)) / 4:
        c += 1
print(c)
```
## 12
```python
from itertools import permutations



def prime(n):
    return all(n % d != 0 for d in range(2, int(n**0.5) + 1))
for n in range(1, 100):
    if prime(n):
        for i in permutations("0" * 21 + "2" * 11 + "1" * n):
            s = ">" + "".join(i)
            while ">1" in s or ">2" in s or ">0" in s:
                if ">1" in s:
                    s = s.replace(">1", "22>", 1)
                if ">2" in s:
                    s = s.replace(">2", "2>", 1)
                if ">0" in s:
                    s = s.replace(">0", "1>", 1)
            if sum(int(i) for i in s if i != ">") % n == 0:
                print(n)
```
## 13
```python
from ipaddress import *
c = 0
ans = []
for m in range(33):
    net1 = ip_network(f"154.63.206.129/{m}", 0)
    net2 = ip_network(f"154.63.100.75/{m}", 0)
    #if net1.network_address == net2.network_address:

net = ip_network(f"154.63.206.129/255.255.0.0", 0)
for ip in net:
    if bin(int(ip))[2:].zfill(32).count("1") % 2 == 0:
        print(ip)
        c += 1

print(c)
```
## 14
```python
alph = '0123456789ABC'

for x in alph:
    n = int(f'615{x}483', 13) + int(f'85996{x}262', 13) + \
        int(f'62421{x}', 13) + int(f'45{x}61584{x}', 13)
    if n % 12 == 0:
        print(n // 12)
        break
```
## 15
```python
print(min(a for a in range(100) if all((x * y < a) or (x < y) or (9 < x) for x in range(100) for y in range(100))))
```
## 16
```python
from sys import setrecursionlimit

setrecursionlimit(3000)
def f(n):
    if n >= 1900:
        return 1
    if n < 1900 and n % 3 != 0:
        return n * f(n + 1)
    else:
        return n * f(n + 2) / 3

print(f(1875)//f(1880))
```
## 17
```python
a = [int(i) for i in open("tmp.txt")]

ans = []

for x, y in zip(a, a[1:]):
    if x % 65 == min(a) and y % 65 == min(a):
        ans.append(x+y)
print(len(ans), max(ans))
```
## 19-21
```python
def F(s, n):
    if s >= 59: return n % 2 == 0
    if n == 0: return 0
    h = [F(s+1, n-1), F(s+4,n-1), F(s*3,n-1)]
    return any(h) if n % 2 != 0 else all(h)



print(f"19. {[s for s in range(1, 59) if F(s, 2)]}")
print(f"20. {[s for s in range(1, 59) if not F(s, 1) and F(s, 3)]}")
print(f"21. {[s for s in range(1, 59) if not F(s, 2) and F(s, 4)]}")
```
## 23
```python
def f(x, end):
    if x > end:
        return 0
    if x == 15 or x == 30:
        return 0
    if x == end:
        return 1
    return f(x+2, end) + f(x+3, end) + f(x**2, end)
print(f(3, 10) * f(10, 20) * f(20, 38))
```
## 24
```python
s = open("tmp.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if all(c.count(i) <= 8 for i in "AEOUIY"):
            m = max(m, len(c))
        else:
            break
print(m)
```
## 25
```python
for a in range(10):
    for b in range(10):
        for c in range(10):
            s = f"12{a}345{b}67089{c}"
            if int(s) % 206 == 0:
                print(int(s), int(s) // 206)
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