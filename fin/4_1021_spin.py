from collections import deque
import copy

items = deque()
order =[]
count =0

N, M = map(int, input().split(' '))
for i in range(0,N):
    items.append(i+1)

for j in map(int, input().split(' ')):
    order.append(j)

for i in range(len(order)):

    left = 0
    right = 0

    if items[0] == order[i]:
        items.popleft()
    else:
        items2 = copy.deepcopy(items)

        while items2[0] != order[i]:
            items2.rotate(1)
            right += 1
        while items[0] != order[i]:
            items.rotate(-1)
            left += 1
        if right>=left:
            count += left
        else:
            count += right
            items=items2
        items.popleft()

print(count)