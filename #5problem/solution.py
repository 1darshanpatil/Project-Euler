import math as m
end_number = 20
cnt = 1
a, b = 1, 2
while cnt < end_number:
    a = m.lcm(a, b)
    b += 1
    cnt += 1
print(a)
