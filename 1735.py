def gcd(x, y):
    while(y != 0):
        r = x % y
        x = y
        y = r

    return x


if __name__ == '__main__':
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())

    tmp1 = a1*b2 + a2*b1
    tmp2 = b1*b2
    n = gcd(tmp1, tmp2)
    print(tmp1//n, tmp2//n)


