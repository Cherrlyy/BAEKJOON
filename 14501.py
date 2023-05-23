def consult(n):
    dp = [0 for i in range(n)]
    for i in range(n):
        for j in range(i+l[i][0]-1, n):
            dp[j] = max(dp[j], dp[i-1]+l[i][1])

    return dp[n-1]


if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    print(consult(n))

# dp는 상태이고, 상태는 곧 구하는 것임. 고로 여기서 상태는 최대 이익, i는 날짜
# 왜 DP 문제인가 하면 날짜와 상담을 늘려가며 달라지는 이익을 바라봤을 때
# 일자별 최대를 구하면 n일 최대도 구할 수 있음을 알 수 있다.
# 점화식을 구하는 방법은 날짜를 늘려가며(방향성과 규칙성 O) 바라볼 때
# 최대 이익에 변화가 생기는 순간을 바라본다.
# 상담이 종료되는 날마다 최대 이익이 변화하는 가능성이 생긴다.
# 그러면 이전과 비교하면 되겠지?
# 처음엔 상담기간과 상담일을 보느라 이차배열로 만들었으나
# 중복되는 부분을 없앤다면 일차배열로 구현 가능함을 알고 고쳤음.
