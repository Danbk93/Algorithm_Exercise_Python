from itertools import combinations

a, b = map(int,input().split(' '))

lab = [[int(x) for x in input().split()]for y in range(a)]
test_lab = [[0 for col in range(b)] for row in range(a)]

count = 0
best_count = 0

zero =[]
virus =[]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(0,a):
    for j in range(0,b):
        test_lab[i][j] = lab[i][j]


def virus(vx, vy):
    for j in range(0, 4):
        nx = int(vx) + dx[j]
        ny = int(vy) + dy[j]
        if 0 <= nx < a and 0 <= ny < b:
            if test_lab[nx][ny] == 0:
                test_lab[nx][ny] = 2
                virus(nx,ny)


for i in range(0,a):
    for j in range(0,b):
        if lab[i][j]==0:
            zero.append(str(i)+' '+str(j))

comb = list(combinations(zero,3))

for row in comb:
    x, y, z = row[0],row[1],row[2]
    x1, x2 = map(int, x.split(' '))
    y1, y2 = map(int, y.split(' '))
    z1, z2 = map(int, z.split(' '))

    test_lab[x1][x2] = 1
    test_lab[y1][y2] = 1
    test_lab[z1][z2] = 1

    for i in range(0, a):
        for j in range(0, b):
            if test_lab[i][j] == 2:
                virus(i, j)

    # for row in test_lab:
    #     print(row)
    # print('')

    for i in range(0, a):
        for j in range(0, b):
            if test_lab[i][j] == 0:
                count += 1

    if best_count <= count:
        best_count = count

    count = 0

    for i in range(0, a):
        for j in range(0, b):
            test_lab[i][j] = lab[i][j]

print(best_count)