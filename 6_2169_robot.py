
a, b = map(int,input().split(' '))

mapd = [[0 for col in range(b+1)] for row in range(a+1)]
d = [[0 for col in range(b+1)] for row in range(a+1)]
tmp = [[0 for col in range(b+1)] for row in range(2)]
line =[]
for i in range(1,a+1):
    line.append(map(int, input().split()))
    for j in range(1, b + 1):
        mapd[i][j] = line[j-1]

print(mapd)

d[1][1] = mapd[1][1]
for j in range(2, b+1):
    d[1][j] = map[1][j] + d[1][j-1]


for i in range(2, a+1):
    tmp[0][0] = d[i-1][1]
    for j in range(1, b+1):
        tmp[0][j] = max(tmp[0][j - 1], d[i - 1][j]) + mapd[i][j]

    tmp[1][b + 1] = d[i - 1][b]
    for j in range(b,0,-1):
        tmp[1][j] = max(tmp[1][j + 1], d[i - 1][j]) + mapd[i][j]

    for j in range(1,b+1):
        d[i][j] = max(tmp[0][j], tmp[1][j])

print(d)

