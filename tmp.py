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

f = open("tmp.txt")

N, K = map(int, f.readline().split())

boxes = []

for i in f:
    size, color = i.split()
    boxes.append([int(size), color])
boxes.sort(reverse=True)

max_zep = [0] * N

for i in range(N):
    prev_zep = [max_zep[j] for j in range(i) if boxes[j][0] - boxes[i][0] >= K and boxes[i][1] != boxes[j][1]]
    if prev_zep:
        max_zep[i] = max(prev_zep) + 1
    else:
        max_zep[i] = 1

mx = max(max_zep)
print(mx, [boxes[i][0] for i in range(N) if max_zep[i] == mx])
"""
