import math
def four_squares(n):
    dp = [0 for x in range(n+1)]
    dp[1:4] = [1, 2, 3]
    j = 2
    for i in range(4, n+1):
        tmp = []
        if i == j ** 2:
            j += 1
            dp[i] = 1
        else:
            for k in range(1, j):
                tmp.append(1+dp[i-k**2])
            dp[i] = min(tmp)

    return dp[n]



if __name__ == "__main__":
    n = int(input())

    print(four_squares(n))