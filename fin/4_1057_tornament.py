import math
num, a, b = map(int, input().split(' '))
count =0
while a!=b:
    a = math.ceil(a/2)
    b = math.ceil(b/2)
    count +=1
print(count)