T = int(input())

while T > 0:
    N, L, k = map(int, input().split(' '))
    road = {}
    while N > 0:
        p, a = map(int, input().split(' '))
        road[a]=p


        N -= 1

    T -= 1