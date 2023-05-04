def coin():
    for i in range(n):
        if a[i] > k:
            m = i - 1
            break
    else:
        m = n - 1


    rem = k
    ans = 0

    for i in range(m, -1, -1):
        ans += rem // a[i]
        rem = rem % a[i]

    return ans

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = []
    for i in range(n):
        a.append(int(input()))

    print(coin())
