def num_lived(k, n):
    x = 0
    if cache[k][n] != 0:
        return cache[k][n]

    if k == 0:
        cache[k][n] = n
        return n

    if n == 1:
        x = num_lived(k - 1, 1)
        cache[k][n] = x
        return x

    for i in range(n):
        x += num_lived(k - 1, i + 1)

    cache[k][n] = x
    return x



if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        k = int(input())
        n = int(input())
        cache = [[0 for i in range(n+1)] for j in range(k+1)]
        print(num_lived(k, n))



        # 리스트 돌면서 해당 칸이 0이 아니면 연산 없이 바로 리턴
        # 0인 경우, 한번만 초기화한다고 생각


