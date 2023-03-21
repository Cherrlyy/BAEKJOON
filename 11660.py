def part_sum(x1, y1, x2, y2):
    x1 = x1-1
    y1 = y1-1
    x2 = x2-1
    y2 = y2-1


    sum = new_table[x2][y2]

    if x1 == 0 and y1 != 0:
        sum -= new_table[x2][y1-1]
    elif x1 != 0 and y1 == 0:
        sum -= new_table[x1-1][y2]
    elif x1 != 0 and y1 != 0:
        sum = sum - new_table[x2][y1 - 1] - new_table[x1 - 1][y2] + new_table[x1 - 1][y1 - 1]

    return sum

if __name__ == '__main__':

    n, m = map(int, input().split())

    table = []
    new_table = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        table.append(list(map(int, input().split())))

    for i in range(n):
        for j in range(n):
            new_table[i][j] = sum(table[i][:j+1])

    for i in range(n):
        for j in range(1, n):
            new_table[j][i] += new_table[j-1][i]

    for i in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(part_sum(x1, y1, x2, y2))

