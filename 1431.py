def serial(l):
    new = []
    for s in l:
        tmp = 0
        for i in s:
            if i in (str(x) for x in range(10)):
                tmp += int(i)
        new.append((len(s), tmp, s))

    new.sort()

    return [x[2] for x in new]


if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(input())

    print(*serial(nums), sep='\n')