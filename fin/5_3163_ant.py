import operator
import collections
import sys
T = int(sys.stdin.readline())
print(T)
d=collections.deque()
while T > 0: #T 받아오기
    N, L, k = int(sys.stdin.readline().rstrip()).split()
    road = []
    answer=[]
    # 모든 배열을 road라는 딕셔너리에 저장하는데 a 가 음수일 경우에 현재 위치(p) 그대로 저장하고 a가 양수일때는 전체 도로 길이에서 현재 위치를 빼서(L-p) 저장.
    # 동시에 d라는 양방향 큐에 하나하나 쌓는다.
    for i in range(N):
        p, a = int(sys.stdin.readline()).split()
        if a < 0:
            road.append([p,a])
            d.append(a)
        else:
            road.append([L-p, a])
            d.append(a)

    road.sort()

    # 정렬된 sortedArr의 1번쨰 열을 비교하여 같으면 d 양뱡향큐에서 양쪽을 pop하고 둘을 비교하여 왼쪽이 크면 오른쪽을 먼저 반대 경우에는 왼쪽을 먼저 now list에 넣는다.
    # 다른 경우에는 sortedArr의 0번째 열이 0보다 작을 때 왼쪽에서 pop 하고 반대 경우에는 오른쪽에서 pop 을 하고 now  list에 넣는다.
    # print(d)
    # print(road)
    i=0
    while i<N:
        if i!=N-1 and int(road[i][0]) == int(road[i+1][0]):
            left = d.popleft()
            right = d.pop()
            if left>right:
                answer.append(right)
                answer.append(left)
            else:
                answer.append(left)
                answer.append(right)
            i +=1
        else:
            if int(road[i][1]) < 0:
                answer.append(d.popleft())
            else:
                answer.append(d.pop())
        i += 1
    # k번째로 떨어지는 개미의 a를 출력한다.
    print(answer[k-1])
    road.clear()
    d.clear()
    answer.clear()
    T -= 1