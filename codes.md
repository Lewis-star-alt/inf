## 1
```python
from itertools import permutations

a = "56 378 26 68 17 134 258 247".split()
s = "GH HD DF DE EB AB AG AC CF BC".split()

print("1 2 3 4 5 6 7 8")
for p in permutations("ABCDEFGH"):
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
                f = (y <= x) and (not(z)) and w
                if f:
                    print(x, y, w, z)
```
## 5
```python
for n in range(1000):
    r = oct(n)[2:]
    s = sum(map(int, r))
    if s % 2 == 0:
        r = r[0] + r + r[0]
    else:
        r += r[-1]
    r = int(r, 8)
    if r < 1100:
        print(n)
```
## 6
```python
from turtle import *

screensize(10000, 10000)
tracer(0)
m = 30
for _ in range(5):
    rt(45)
    fd(10 * m)
    rt(45)

for _ in range(6):
    fd(20 * m)
    rt(90)

up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * m, y * m)
        dot(3, "blue")
update()
exitonclick()
```
## 8
```python
from itertools import product, permutations

words = sorted(list(set(permutations("АААВВРР"))))


for i, w in enumerate(words):
    i += 1
    w = "".join(w)
    if i % 2 == 0 and w[0] == "В" and "ААА" in w and "РР" not in w:
        print(i, w)
```
## 9
```python
c = 0
for line in open("tmp.txt"):
    a = [int(i) for i in line.split()]
    p = [i for i in a if a.count(i) > 1]
    m = max(a)
    if len(p) > 1 and m not in p and sum(p) < m:
        c += 1
print(c)
```
## 12
```python
ans = []
for n in range(3, 10001):
    s = "1" + "2" * n
    while "12" in s or "322" in s or "222" in s:
        if "12" in s:
            s = s.replace("12", "2", 1)
        if "322" in s:
            s = s.replace("322", "21", 1)
        if "222" in s:
            s = s.replace("222", "3", 1)
    ans.append(sum(map(int, s)))
print(max(ans))
```
## 13
```python
from ipaddress import ip_network

c = 0
net = ip_network("106.184.0.0/255.248.0.0", 0)

for ip in net:
    if bin(int(ip))[2:].count("1") % 2 != 0:
        c += 1
print(c)
```
## 14
```python
for x in range(1, 2031):
    n = 6 ** 260 + 6 ** 160 + 6 ** 60 - x
    s = ""
    while n:
        s += str(n % 6)
        n //= 6
    if s.count("0") == 202:
        print(x)
        break
```
## 15
```python
print(min(a for a in range(1, 5000) if all((x & 2735 != 0) <= ((x & 1234 == 0) <= (x & a != 0)) for x in range(1, 5000))))
```
## 16
```python
from sys import setrecursionlimit

setrecursionlimit(3000)
def f(n):
    if n == 6:
        return 1
    if n > 1:
        return 3 * n + 2 + f(n - 1)

print(f(2024) - f(2020))
```
## 17
```python

```
## 19-21
```python
def F(s, n):
    if s >= 82: return n % 2 == 0
    if n == 0: return 0
    h = [F(s+2, n-1), F(s+4,n-1), F(s*3,n-1)]
    return any(h) if n % 2 != 0 else all(h)



print(f"19. {[s for s in range(1, 82) if F(s, 2)]}")
print(f"20. {[s for s in range(1, 82) if not F(s, 1) and F(s, 3)]}")
print(f"21. {[s for s in range(1, 82) if not F(s, 2) and F(s, 4)]}")
```
## 23
```python
from sys import setrecursionlimit

setrecursionlimit(30000000)


def f(x, end, n):
    if x > end + 1:
        return 0
    if x % 10 == 0:
        return 0
    if x == 65:
        return 1
    if x == end:
        return 1
    if n == 1:
        return f(x+2, end, n-1) + f(x*3, end, n-1)
    return f(x+2, end, n+1) + f(x*3, end, n) + f(x-1, end, n)
print(f(5, 32, 0) * f(32, 62, 0))
```
## 25
```python
def m(n):
    div = set()
    for d in range(2, int(n**0.5)+1):
        if n % d == 0:
            div.add(d)
            div.add(n // d)
    if div:
        return min(div) + max(div)
    return 0

for n in range(800_000, 800_100):
    M = m(n)
    if M % 10 == 4:
        print(n, M)
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