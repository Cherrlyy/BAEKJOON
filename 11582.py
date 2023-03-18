def sort_scores(n, k, chickens):
    while n != 1:
        n = n//2

        new = [chickens[i:i+len(chickens)//n] for i in range(0, len(chickens), len(chickens)//n)]
        tmp = []
        for i in range(len(new)):
            new[i].sort()
            tmp.extend(new[i])

        if n == k:
            return tmp
        chickens = tmp


if __name__ == '__main__':
    n = int(input())

    chickens = list(map(int, input().split()))

    k = int(input())

    print(*sort_scores(n, k, chickens))