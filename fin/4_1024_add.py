N, L = map(int, input().split(' '))
# 수학공식을 적용하여 거꾸로 풀자
x = -1
t= -1
temp = -1
for i in range(L,101):
    t = ((i - 1) * i) / 2

    if (N-t)%i==0 and (N - t) / i>=0:
        x = (N - t) / i
        temp = i
        break


if x==-1:
    print(int(-1))
else:
    for j in range(0,temp):
        print(int(x+j),end=' ')
