import sympy as smp

which_prime = 10001

lst = []
i = 1
while len(lst) < which_prime:
    if smp.isprime(i):
        lst.append(i)
    i += 1
print(lst[-1])
