from itertools import combinations

num = int(input())

b = num/2
count=0
for i in range(0,int(b)):
    comb = list(combinations(num, i))

print(comb)



print(count/10007)