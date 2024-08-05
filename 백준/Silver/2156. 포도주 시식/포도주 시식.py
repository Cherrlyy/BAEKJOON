n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
    
dp = [0 for _ in range(n)]
dp[0] = l[0]

for i in range(1, n):
    if i == 1: dp[1] = dp[0] + l[1]
    else:
        dp[i] = max(dp[i-1], dp[i-2] + l[i], l[i] + l[i-1] + dp[i-3])

print(dp[n-1])