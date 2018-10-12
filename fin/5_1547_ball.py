T = int(input())
ball= 1
while T > 0:
    X, Y = map(int, input().split(' '))
    if ball == X:
        ball =Y
    elif ball ==Y:
        ball =X

    T -= 1
print(ball)