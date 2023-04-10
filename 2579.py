def max_score(i, seq):
    if i < 0:
        ans = 0
    else:
        if dp[seq-1][i] != 0:
            return dp[seq-1][i]
        if seq == 1:
            ans = max(max_score(i-1, 2), max_score(i-2, 1)) + scores[i]
        if seq == 2:
            ans = max_score(i-2, 1) + scores[i]
        dp[seq-1][i] = ans
    return ans

if __name__== '__main__':
    n = int(input())
    scores = []
    for i in range(n):
        scores.append(int(input()))
    dp = [[0 for i in range(n)] for j in range(2)]
    print(max_score(len(scores)-1, 1))