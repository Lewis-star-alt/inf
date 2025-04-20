def prime(n):
    return all(n % d != 0 for d in range(2, int(n**0.5) + 1))
for n in range(2, 100):
    if prime(n):
            s = ">" + "0" * 21 + "2" * 11 + "1" * n
            while ">1" in s or ">2" in s or ">0" in s:
                if ">1" in s:
                    s = s.replace(">1", "22>", 1)
                if ">2" in s:
                    s = s.replace(">2", "2>", 1)
                if ">0" in s:
                    s = s.replace(">0", "1>", 1)
            if sum(int(i) for i in s if i != ">") % n == 0:
                print(n)