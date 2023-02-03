def isin(numList, XList):
    for x in XList:
        ans = 0
        if x in numList:
            ans = 1
        print(ans)


if __name__ == '__main__':
    n = map(int, input())
    numList = set(map(int, input().split()))
    m = map(int, input())
    XList = list(map(int, input().split()))

    isin(numList, XList)
