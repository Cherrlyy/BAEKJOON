def print_stars(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ',end='')
        for j in range(i+1):
            print('*', end='')
        print()


if __name__ == '__main__':
    n = int(input())
    print_stars(n)
