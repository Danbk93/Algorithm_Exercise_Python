
N, M = map(int, input().split(' '))
order =[]
items =[]
count =0
orders = input().split(' ')
pointer =1

for i in range (0,M):
    order.append(int(orders[i]))

for j in range(0,N):
    items.append(j+1)

for k in range (0,len(order)):

    if k >N
    for l in range(0, len(items)):
        if order[k]== items[l]:
            count += l
            items.remove(l)

