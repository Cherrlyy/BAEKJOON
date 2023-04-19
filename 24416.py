def cnt_run(n):
    # code1
    num = [0 for i in range(n + 1)]
    num[1], num[2] = 1, 1
    for i in range(3, n + 1):
        num[i] = num[i - 1] + num[i - 2]
    print(num[n], end=' ')
    # code2
    print(n - 2)


if __name__ == "__main__":
    n = int(input())

    cnt_run(n)