"""
f = open("tmp.txt")

n = f.readline()
data = [list(map(int, i.split())) for i in f]
print(n)
data.sort(key=lambda x: x[1])

ans = [data.pop()]
for i in data:
    if i[0] >= ans[-1][1]:
        ans.append(i)
print(len(ans))


f = open("tmp.txt")
k = int(f.readline())
n = int(f.readline())
cell = [[] for _ in range(k)]
data = [list(map(int, i.split())) for i in f]
data.sort()

for i in data:
    for j in range(k):
        if (not cell[j]) or (i[0] > cell[j][-1][1]):
            cell[j].append(i)
            break
c = 0
for i in cell:
    c += len(i)
print(c)
"""
