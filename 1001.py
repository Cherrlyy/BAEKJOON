def minus(a, b):
    return a-b

if __name__ == '__main__':
    tmpList = list(map(int, input().split()))

    print(minus(tmpList[0], tmpList[1]))