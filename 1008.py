def division(a, b):
    if b != 0:
        return a/b

if __name__ == '__main__':
    tmpList = list(map(int, input().split()))

    print(division(tmpList[0], tmpList[1]))