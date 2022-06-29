ans = []
sm = 0
max_fib = 4*10**6
#1 million = 10^6
i = 2
lst = [1, 2]
nth_fib = lst[-1]
while nth_fib < max_fib:
    lst.append(lst[i - 2] + lst[i - 1])
    nth_fib = lst[-1]
    i += 1
#print(lst)
final_sequence = lst[:-1]
#print(final_sequence)
ans = sum([nth for nth in final_sequence if nth%2 == 0])
print(ans)
