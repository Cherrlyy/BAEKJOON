def d():
    selfNumber = set()
    for i in range(1, 10001):
        tmp = i
        for j in str(i):
            tmp = tmp + int(j)
        selfNumber.add(tmp)
    return [i for i in range(1, 10001) if i not in selfNumber]


if __name__ == '__main__':
    print(*d(), sep='\n')