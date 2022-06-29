r = range(1, 10**3)
found = False
for a in r:
    for b in r:
        c = (10**3 - a - b)**2
        if a**2 + b**2 == c:
            print(a*b*c)
            found = True
        if found == True:
            break
            
            
#-----------------------------------------O(n)-------------------------------------#
#for _ in range(int(input())):
#    n = int(input())
#    m = -1
#    if n%2 != 1:
#        for a in range(1, n//3):
#            b = n*(n - 2*a)//(2*(n - a))
#            c = n - a - b
#            if a**2 + b**2 == c**2:
#                m = max(m, a*b*c)
#    print(m)
