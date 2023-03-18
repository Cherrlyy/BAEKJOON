def is_prime(m, n):
    l1 = [x for x in range(2, n+1)]
    l2 = l1
    for i in l2:
        for j in l2:
            if j % i == 0 and j != i:
                l1.remove(j)
    sum = 0
    min = n
    for i in l1:
        if i >= m:
            sum+=i
            if min > i:
                min = i

    if sum == 0:
        print(-1)
    else:
        print(sum)
        print(min)

if __name__ == '__main__':
    m = int(input())
    n = int(input())

    is_prime(m, n)