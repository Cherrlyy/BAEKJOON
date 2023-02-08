def print_sol(a, b, m):
    ans = [[i[k]+j[k] for k in range(m)] for i,j in zip(a, b)]
    return ans

if __name__ == '__main__':
    n, m = map(int, input().split())
    matrix_a = [list(map(int, input().split())) for i in range(n)]
    matrix_b = [list(map(int, input().split())) for i in range(n)]

    ans = print_sol(matrix_a, matrix_b, m)
    for x in ans:
        print(*x)