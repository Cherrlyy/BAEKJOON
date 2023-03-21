if __name__ == '__main__':
    n, m = map(int, input().split())
    l1 = set()
    for i in range(n):
        l1.add(input())

    l2 = set()
    for i in range(m):
        l2.add(input())

    ans = list(l1 & l2)
    ans.sort()

    print(len(ans))
    for e in ans:
        print(e)