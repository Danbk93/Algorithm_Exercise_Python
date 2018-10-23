a, b = map(int,input().split(' '))

board = [[int(x) for x in input().split()]for y in range(a)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


for i in range(0,a):
    for j in range(0, b):
        if board[i][j]== 'R':
            rx = i
            ry = j
        elif board[i][j]== 'B':
            bx = i
            by = j

def searching():
    for j in range(0, 4):
        nrx = rx + dx[j]
        nry = ry + dy[j]
        nbx = bx + dx[j]
        nby = by + dy[j]
        if board[nrx][nry] == '#':
