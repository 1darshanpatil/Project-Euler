import math as m

def isprime(N):
    if N in [0, 1]:
        return False
    if N in [2, 3, 5, 7]:
        return True
    else:
        for x0 in range(2, m.ceil(m.sqrt(N)) + 1):
            if N%x0 == 0:
                return False
    return True
given_number = 600851475143                                          #This

for small_divisor in range(2, given_number):
    if given_number%small_divisor == 0:
        large_divisor = given_number//small_divisor
        if isprime(large_divisor):
            print(large_divisor)
            break
