num = int(input())


dp = [0] * num

for i in range(2,num+1):
    dp[i] = dp[i-1]+1
    print(dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[int(i / 3)] + 1)

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[int(i / 2)] + 1)

print(dp[num+1])