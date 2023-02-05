def alarm(h, m):
    if m >= 45:
        m = m - 45
    else:
        h = h -1
        m = 60 - (45 - m)
    if h < 0:
        h = 24 + h

    return [h, m]


if __name__ == '__main__':
    h, m = list(map(int, input().split()))

    print(*alarm(h, m))