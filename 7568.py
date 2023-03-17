def ordered_size():
    for i in range(len(l)):
        order = 0
        x, y = l[i][0], l[i][1]

        for j in range(len(l)):
            if i == j:
                continue

            if x < l[j][0] and y < l[j][1]:
                order+=1

        print(order+1, end=' ')





if __name__ == '__main__':
    n = int(input())

    l = []
    for i in range(n):
        l.append(list(map(int, input().split())))

    ordered_size()


    # x, y 둘다 커야함
