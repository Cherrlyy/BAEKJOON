def num_lived(k, n):
    if cache[k][n] != 0:
        return cache[k][n]

    if k == 0:
        cache[k][n] = n
        return n

    if n == 1:
        x = num_lived(k - 1, 1)
        cache[k][n] = x
        return x

    x = num_lived(k, n-1) + num_lived(k-1, n)
    cache[k][n] = x

    return x



if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        k = int(input())
        n = int(input())
        cache = [[0 for i in range(n+1)] for j in range(k+1)]
        print(num_lived(k, n))





