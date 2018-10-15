import operator
import collections
T = int(input())
d=collections.deque()
while T > 0:
    N, L, k = map(int, input().split())
    road = {}
    now=[]
    for i in range(N):
        p, a = map(int, input().split())
        if a < 0:
            road[a] = p
            d.append(a)
        else:
            road[a] = L-p
            d.append(a)
    sortedArr = sorted(road.items(), key=operator.itemgetter(1))

    for i in range(0,N-1):
        if int(sortedArr[i][1]) == int(sortedArr[i+1][1]):
            left = d.popleft()
            right = d.pop()
            if left>right:
                now.append(right)
                now.append(left)
            else:
                now.append(left)
                now.append(right)
            i +=1
        else:
            if int(sortedArr[i][0]) < 0:
                now.append(d.popleft())
            else:
                now.append(d.pop())

    print(now[k-1])
    road.clear()
    d.clear()
    T -= 1