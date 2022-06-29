from sympy import isprime
last = 2*10**6
i = 1
sm = 0
while i<last:
    if isprime(i):
        sm += i
    i += 1
print(sm)
