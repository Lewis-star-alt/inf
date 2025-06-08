## 1
```python
from itertools import permutations

a = "23467 1356 12458 13 238 127 16 35".split()
s = "ab ac bc bd cd de cg eg ef fg gh ch".split()

print("1 2 3 4 5 6 7 8")
for p in permutations("abcdefgh"):
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
                f = ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))
                if f :
                    print(x, y, w, z, f)
```
## 5
```python
ans = []
for n in range(1000):
    r = bin(n)[2:]
    s = sum(map(int, r)) % 2
    r += str(s)
    s2 = sum(map(int, r)) % 2
    r += str(s2)
    r = int(r, 2)
    if r > 123:
        ans.append(r)
print(min(ans))
```
## 6
```python
from turtle import *

screensize(10000, 10000)
tracer(0)
m = 30

for _ in range(2):
    fd(6 * m)
    rt(90)
    fd(12 * m)
    rt(90)

up()
fd(1 * m)
rt(90)
fd(3 * m)
lt(90)
down()

for _ in range(2):
    fd(77 * m)
    rt(90)
    fd(45 * m)
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
print(((53 * 60 + 30) * 44100 * 16 * 2 + 10 * 512 * 8 * 1024) / 10**8)
```
## 8
```python
from itertools import *

c = 0
for n in product("0123456789ABCD", repeat=5):
    if n[0] != "0" and n.count("9") == 1 and len([i for i in n if i in "BCD"]) <= 3:
        print(n)
        c += 1
print(c)
```
## 9
```python
c = 0
for line in open("tmp.txt"):
    a = [int(i) for i in line.split()]
    if len(a) == len(set(a)) and (max(a) + min(a)) > (sum(a) - min(a) - max(a)):
        c += 1
print(c)
```
## 12
```python
for n in range(1000):
    s = ">" + "0" * 12 + "1" * n + "2" * 8
    while ">1" in s or ">2" in s or ">0" in s:
        if ">1" in s:
            s = s.replace(">1", "22>", 1)
        if ">2" in s:
            s = s.replace(">2", "2>", 1)
        if ">0" in s:
            s = s.replace(">0", "1>", 1)
    sm = sum(int(i) for i in s if i != ">")
    if sm == 68:
        print(n)
```

## 13
```python
from ipaddress import *

c = 0
net = ip_network("94.253.128.0/255.255.128.0", 0)

for ip in net:
    b = bin(int(ip))[2:].zfill(32)
    if b.count("1") % 6 != 0 and b[-3:] == "101":
        print(b)
        c += 1
print(c)
```
## 14
```python
ans = []
c = []
for x in range(10, 7001):
    n = 5 ** 2025 + 5 ** 400 - x
    s = ""
    while n:
        s += str( n % 5)
        n //= 5
    ans.append(s.count("4"))
    if s.count("4") == 399:
        c.append(x)
print(max(ans))
print(max(c))
```
## 15
```python
print(max(a for a in range(1, 1000) if all((x % 33 == 0) <= ((x % a != 0) <= (x % 242 != 0)) for x in range(1, 10000))))
```
## 16
```python
def f(n):
    if n < 3:
        return 1
    if n > 2:
        return f((n + 1) // 2) + 1

print(f(2025))
```
## 17
```python
from math import gcd

a = [int(i) for i in open("tmp.txt")]

ans = []
arr = []
for x, y in zip(a, a[1:]):
    arr.append(gcd(x, y))

cnt = 0
c = dict()
for i in arr:
    for j in arr:
        if  i == j:
            cnt += 1
    c[i] = cnt
    cnt = 0

m = 0
for i in c.items():
    m = max(m, i[1])
for i in c.items():
    if i[1] == m:
        m = i[0]


for x, y in zip(a, a[1:]):
    if gcd(x, y) == m:
        ans.append(x+y)

print(m, max(ans))

```
## 19-21
```python
def F(s1, s2, n):
    if s1 + s2 >= 227: return n % 2 == 0
    if n == 0: return 0
    h = [F(s1+1, s2, n-1), F(s1*2, s2, n-1), F(s1, s2+1, n-1), F(s1, s2*2, n-1)]
    return any(h) if n % 2 != 0 else all(h)


print(f"19. {[s for s in range(1, 210) if F(17, s, 2)]}")
print(f"20. {[s for s in range(1, 210) if not F(17, s, 1) and F(17, s, 3)]}")
print(f"21. {[s for s in range(1, 210) if not F(17, s, 2) and F(17, s, 4)]}")
```
## 23
```python
def f(n, end):
    if n < end:
        return 0
    if n == end:
        return 1
    return f(n-2, end) +  f(n//2, end)

print(f(32,14) * f(14, 1))
```
## 24
```python
import re

s = open("tmp.txt").readline()
num = r"(?:[1-9][0-9]*|0)"
pr = rf"(?:(?:{num}\*)*0(?:\*{num})*)"

pattern = rf"{pr}(?:\+{pr})*"

print(max([len(c) for c in re.findall(pattern, s)]))
```
## 25
```python
def divs(n):
    d = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n %  i == 0:
            d.add(i)
            d.add(n // i)
    if d:
        return min(d) + max(d)
    return 0

for i in range(800000, 810000):
    if divs(i) % 10 == 4:
        print(i, divs(i))
        input()
```
## 26
```python
f = open("tmp.txt")
n = int(f.readline())
st = n // 4
data = [list(map(int,s.split())) for s in f]
data.sort(key = lambda x: x[0])
s = [x for x in data if x[1:].count(2)==0]
ns = [x for x in data if x[1:].count(2)!=0]

s.sort(key = lambda x: sum(x[1:]),reverse=True)
ns.sort(key = lambda x: x[1:].count(2))
rating = s + ns

ans = []
for i in data:
    if i.count(2) == 3:
        ans.append(i[0])
print(rating[st - 1][0], min(ans))
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
        sosed = [p1 for p1 in data if dist(p, p1) < 0.7]
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
print(int(px * 10000), int(py * 10000))
```