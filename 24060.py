def blackjack(m, numList):
    numList = sorted(numList, reverse=True)
    max = 0
    for i in range(len(numList)):
        for j in range(i+1, len(numList)):
            for k in range(j+1, len(numList)):
                tmp = numList[i] + numList[j] + numList[k]
                if tmp <= m and tmp > max:
                    max = tmp

    return max







if __name__ == '__main__':
    n, m = map(int, input().split())
    numList = map(int, input().split())

    print(blackjack(m, numList))

