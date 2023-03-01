def zero_one_num(n):
    if len(table) == n+1:
        return table[n]
    for i in range(len(table), n+1):
        table.append([x+y for x, y in zip(table[i-1], table[i-2])])

    return table[n]


if __name__ == '__main__':
    t = int(input())

    table = []
    table.append([1, 0])
    table.append([0, 1])

    for i in range(t):
        print(*zero_one_num(int(input())))
