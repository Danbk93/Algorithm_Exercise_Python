T = int(input())
dragon = [[0 for col in range(102)] for row in range(102)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
result =0

while T > 0:
    y, x, d, g = map(int,input().split(' '))

    st = []

    end_x = x
    end_y = y
    dragon[end_x][end_y] = 1

    end_x = x + dx[d]
    end_y = y + dy[d]
    dragon[end_x][end_y] = 1

    st.append(d)

    for i in range(0,g):

        size = len(st)
        for j in range(size-1,-1,-1):
            dir =(st[j]+1)%4
            end_x = end_x + dx[dir]
            end_y = end_y + dy[dir]
            dragon[end_x][end_y] = 1
            st.append(dir)

    T -= 1


# for row in dragon:
#     print(row)

for i in range(0,101):
    for j in range(0, 101):
        if dragon[i][j] == 1 and dragon[i][j + 1] == 1 and dragon[i + 1][j] == 1 and dragon[i + 1][j + 1] == 1:
            result += 1


print(result)