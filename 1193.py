def find_fraction(n):
    sum = 0
    for i in range(1, 10000000):
        sum+=i
        if sum >= n:
            break

    if i % 2 == 0:
        return str(i - (sum-n))+'/'+str((sum-n)+1)

    else:
        return str((sum-n)+1)+'/'+str(i - (sum-n))


if __name__ == '__main__':
    n = int(input())

    print(find_fraction(n))