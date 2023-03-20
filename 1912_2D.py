def sequence_sum(n, l):
#     경우의 수는 nC2와 같음
#       테이블 생성해서 행을 시작점, 열을 종점으로
#       각 칸에는 합 등록
#       2개짜리 초기화 하고 나머진 for문으로 등록
    table = [[0 for x in range(i+1)] for i in range(n)]

    max = -1000*n

    for i in range(n):
        table[i][i] = l[i]
        if table[i][i] > max:
            max = table[i][i]

    for i in range(n-1):
        table[i+1][i] = l[i+1]+l[i]
        if table[i+1][i] > max:
            max = table[i+1][i]


    for i in range(n):
        for j in range(i):
            if table[i][j] == 0:
                table[i][j] = table[i-1][j] + l[i]
                if table[i][j] > max:
                    max = table[i][j]

    return max

if __name__ == '__main__':
    n = int(input())

    l = list(map(int, input().split()))
    print(sequence_sum(n, l))


