def recursion_to_dp():
    for i in range(21):
        for j in range(21):
            for k in range(21):
                if i == 0 or j == 0 or k == 0:
                    matrix[i][j][k] = 1
                elif i < j and j < k:
                    matrix[i][j][k] = matrix[i][j][k-1] + matrix[i][j-1][k-1] - matrix[i][j-1][k]
                else:
                    matrix[i][j][k] = matrix[i-1][j][k] + matrix[i-1][j-1][k] + matrix[i-1][j][k-1] - matrix[i-1][j-1][k-1]


if __name__ == '__main__':
    matrix = [[[0]*21 for i in range(21)] for j in range(21)]
    recursion_to_dp()
    in_range = lambda x: (0 if x < 0 else x) if x <= 20 else 20

    while True:
        a, b, c = map(int, input().split())
        if a == -1 and b == -1 and c == -1:
            break

        else:
            ans = 0
            if a <= 0 or b <= 0 or c <= 0:
                ans = 1
            elif a > 20 or b > 20 or c > 20:
                ans = matrix[20][20][20]
            else:
                ans = matrix[a][b][c]
            print('w('+str(a)+', '+str(b)+', '+str(c)+') = '+str(ans))


