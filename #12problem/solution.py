import math
def factors_of_x(x):
    facts = []
    for i in range(1, math.ceil(math.sqrt(x)) + 1):
        if x%i == 0 and i not in facts:
            facts.append(i)
            facts.append(x//i)
    fact_set = set(facts)
    return fact_set, len(fact_set)           #To avoid double counting and sorting

def gen_triangle(n):
    return n*(n+1)//2


#print(list(map(gen_trianlge, range(10))))                  Testing😃

n = 1
c = 1
while c < 500:
    triangle = gen_triangle(n)
    temp = factors_of_x(triangle)
    c = temp[1]
    n += 1
print(triangle)
