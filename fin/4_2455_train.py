
count =0
larger_count =0
for i in range(0,4):
    a, b = map(int,input().split(' '))
    count = count+b-a
    if larger_count<count:
        larger_count= count

print(larger_count)