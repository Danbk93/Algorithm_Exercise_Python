from itertools import combinations

a, b = map(int,input().split(' '))

lab =[[int(x) for x in input().split()]for y in range(a)]

count =0
best_count=0

templab =[]
zero =[]
virus =[]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(0,a):
    for j in range(0,b):
        if lab[i][j]==0:
            zero.append(str(i)+' '+str(j))
        elif lab[i][j]==2:
            virus.append(str(i)+' '+str(j))

comb = list(combinations(zero,3))

for row in comb:
    x, y, z = row[0], row[1], row[2]
    x1, x2 = map(int,x.split(' '))
    y1, y2 = map(int,y.split(' '))
    z1, z2 = map(int,z.split(' '))

    lab[x1][x2] = 1
    lab[y1][y2] = 1
    lab[z1][z2] = 1
    templab = lab

## 고치는중
    while templab != lab:
        for i in range(0, len(virus)):
            vx, vy = virus[i].split(' ')
            for j in range(0,4):
                nx = int(vx) + dx[j]
                ny = int(vy) + dy[j]
                if 0 <= nx and nx < a and 0 <= ny and ny < b:
                    if lab[nx][ny] == 0:
                        lab[nx][ny] = 2

            templab = lab


    for row in lab:
        print(row)

    print('')

    for i in range(0, a):
        for j in range(0, b):
            if lab[i][j] == 0:
                count += 1

    if best_count <= count:
        best_count = count


    count =0
    lab[x1][x2] = 0
    lab[y1][y2] = 0
    lab[z1][z2] = 0

print(best_count)

