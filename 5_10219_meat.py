import copy
T = int(input())

while T > 0:
    H, W = map(int, input().split(' '))
    pan = [[x for x in input().split()] for y in range(H)]
    test_pan = [[0 for col in range(W)] for row in range(H)]

    test_pan = copy.deepcopy(pan)

    for i in range(0,H):
        test_pan[i][0] = pan[abs(i-(H-1))][0]
        print(test_pan[i][0])

    T -= 1