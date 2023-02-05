def sum(cycleList, n):
    # print(cycleList)
    if len(cycleList) > 1:
        if cycleList[-1] == cycleList[0]:
            return cycleList
    cycleList.append(n)

    if n < 10:
        tmp = '0' + str(n)
    else:
        tmp = str(n)
    result = int(tmp[1] + str(int(tmp[0]) + int(tmp[1]))[-1])
    return sum(cycleList, result)




if __name__ == '__main__':
    n = int(input())

    print(len(sum([], n))-1)