goal = input()
T = int(input())
a= input().split(' ')
first = 100

broken =[]

for i in range(0,10):
    broken[i] = 0
for j in range(len(a)):
    broken[int(a[j])] = 1

# for i in range(0,500001):
#     if broken[int(goal[i])]==1:
#         ㅈㅈ...

