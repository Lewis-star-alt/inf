from fnmatch import fnmatch

def prime(n):
    return n > 1 and all(n % d != 0 for d in range(2, int(n**0.5)+1))

for i in range(2273, 10**9, 2273):
    if fnmatch(str(i), "5*35?5*1") and prime(sum(map(int, str(i)))):
        print(i, i // 2273)