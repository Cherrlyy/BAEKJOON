import sys
input = sys.stdin.readline

n = int(input())
n_l = list(map(int, input().split()))
m = int(input())
dp = [[0 for j in range(n)] for i in range(n)]

for step in range(n):
    for j in range(n-step):
        start, end = j, j+step
        if step == 0:
            dp[start][end] = 1
        elif step == 1:
            if n_l[start] == n_l[end]:
                dp[start][end] = 1
        else:
            if n_l[start] == n_l[end] and dp[start+1][end-1] == 1:
                dp[start][end] = 1

for i in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])