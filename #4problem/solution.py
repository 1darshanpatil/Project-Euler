r1 = range(100, 10**3)
def pali(n):
    N = str(n)
    if N[::-1] == N: return True
    return False
lst = []
for x in r1:
    for y in r1:
        lst.append(x*y)
lst = set(lst)
lst = sorted(lst, reverse = True)
for x in lst:
    if pali(x):
        print(x); break
