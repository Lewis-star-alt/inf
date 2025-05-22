## 1
```python
from itertools import permutations

a = "38 3457 1258 268 23 47 26 134".split()
s = "AG GH AF GF GD HE ED CD CF CB BF".split()

print("1 2 3 4 5 6 7 8")
for p in permutations("ABCDEFGH"):
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
                f = ((x or y) == (y <= z)) or w
                if f == 0:
                    print(x, y, w, z, f)
```
## 5
```python
ans = []
c = 0
for n in range(1000):
    r = bin(n)[3:]
    if r.count("1") % 2 == 0:
        r = "10" + r
    else:
        r = "1" + r + "0"
    r = int(r, 2)
    if r < 450:
        ans.append(r)
print(max(ans))
```
## 6
```python
from turtle import *

screensize(10000, 10000)
tracer(0)
m = 30

for _ in range(2):
    fd(10 * m)
    rt(90)
    fd(18 * m)
    rt(90)

up()
fd(5 * m)
rt(90)
fd(7 * m)
lt(90)
down()

for _ in range(2):
    fd(10 * m)
    rt(90)
    fd(7 * m)
    rt(90)


up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, "blue")
update()
exitonclick()
print(11 * 19 + 5 * 8)
```
## 7
```python

```
## 8
```python
from itertools import product

c = 0
for n in product("01234567", repeat=6):
    n = "".join(n)
    if n[0] != "0" and "33" not in n and n.count("3") == 2:
        s, f = (i for i in range(len(n)) if n[i] == "3")
        t = n[s+1:f]
        if all(i in "4567" for i in t):
            c += 1
            print(n)
print(c)
```
## 9
```python
c = 0
for line in open("tmp.txt"):
    a = [int(i) for i in line.split()]
    a.sort()
    p = [i for i in a if a.count(i) == 2]
    np = [i for i in a if a.count(i) == 1]
    m = max(a)
    if len(p) == 2 and len(np) == 2 and a[-1] + a[-2] > (a[0] + a[1]) * 2 and max(a) % min(a) != 0:
        c += 1
print(c)
```
## 12
```python
for n in range(1000):
    s = ">2" + n * "12" + "<"
    while ">2<" not in s:
        s = s.replace(">1", ">2", 1)
        s = s.replace("12<", "1<2", 1)
        s = s.replace(">21", "1>", 1)
        s = s.replace("1<", "<2", 1)
    if sum(int(i) for i in s if i != ">" and i != "<") > 103:
        print(n)
        break
```

## 13
```python
from ipaddress import *


for m in range(33):
    net1 = ip_network(f"154.63.206.129/{m}", 0)
    net2 = ip_network(f"154.63.100.75/{m}", 0)
    if net1.network_address == net2.network_address:
        print(net1.network_address)
```
## 14
```python
from string import printable


for p in range(9, 30):
    for x in printable[:p]:
        for y in printable[:p]:
            for z in printable[:p]:
                for w in printable[:p]:
                    if int(f'{z}{x}{y}{x}5', p) + int(f'{x}{y}816', p) == int(f'{w}{z}{x}70', p):
                        print(int(x+y+z+w, p))
```
## 15
```python
def f(x):
    Q = 1745 <= x <= 3089
    P = 1315 <= x <= 2018
    R = 2463 <= x <= 3828
    A = a1 <= x <= a2
    return ((not Q) <= (P or R)) <= ((not A) <= (not Q))

r = []
d = [y for x in (1745, 3089, 1315, 2018, 2463, 3828) for y in (x, x + 0.1, x - 0.1)]
for a1 in d:
    for a2 in d:
        if a2 >= a1 and all(f(x) for x in d):
            r.append(a2-a1)
print(min(r))
```
## 16
```python
from sys import setrecursionlimit
setrecursionlimit(10**7)

def f(n):
    if n < 7:
        return n
    if n >= 7:
        return n + 1 + f(n - 2)


print(f(2024) - f(2020))
```
## 17
```python
a = [int(i) for i in open("tmp.txt")]
m = max(i for i in a if str(abs(i))[0] == "8")

ans = []
for x, y, z in zip(a, a[1:], a[2:]):
    d = [x, y, z]
    cond = sum(1 for i in d if str(abs(i))[0] == "6")
    if cond <= 1 and sum(d) >= m:
        ans.append(sum(d))
print(len(ans), min(ans))
```
## 19-21
```python
def F(s, n):
    if s >= 73: return n % 2 == 0
    if n == 0: return 0
    h = [F(s+3,n-1), F(s+1, n-1), F(s*3, n-1)]
    return any(h) if n % 2 != 0 else all(h)


print(f"19. {[s for s in range(1, 73) if F(s, 2)]}")
print(f"20. {[s for s in range(1, 73) if not F(s, 1) and F(s, 3)]}")
print(f"21. {[s for s in range(1, 73) if not F(s, 2) and F(s, 4)]}")
```
## 23
```python
def f(n, end):
    if n < end:
        return 0

    if n == end:
        return 1
    return f(n-3, end) + f(n//3, end) + f(n-2, end)

print(f(43,21) * f(21, 15) * f(15, 13))
```
## 24
```python
s = open("tmp.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l+m, len(s)):
        c = s[l:r+1]
        if c.count("Y") <= 150:
            m = max(m, len(c))
        else:
            break
print(m)
```
## 25
```python
from fnmatch import fnmatch

for i in range(2025, 10**8, 2025):
    if fnmatch(str(i), "12*34?5"):
        print(i, i // 2025)
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
print(int(px * 100000), int(py * 100000))
```