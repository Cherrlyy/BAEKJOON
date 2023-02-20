def repeat_str(l):
    m = int(l[0])
    for j in l[1]:
        for i in range(m):
            print(j, end='')
    print()


if __name__ == '__main__':
    n =int(input())

    for i in range(n):
        tmp_list = input().split()
        repeat_str(tmp_list)