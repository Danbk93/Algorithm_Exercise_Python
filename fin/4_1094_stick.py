x = int(input())
stick =64
count =0
while x>0:
    if stick>x:
        stick /= 2
    else:
        count +=1
        x -= stick


print(count)



