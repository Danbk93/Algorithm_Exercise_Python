
N, M = map(int, input().split(' '))
order =[]
items =[]
orders = input().split(' ')

for i in range (0,M):
    order.append(int(orders[i]))

for j in range(0,N):
    items.append(j+1)

for k in range (0,len(order)):
    for l in range(0, len(items)):
        



