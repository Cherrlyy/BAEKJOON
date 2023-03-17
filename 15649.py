from itertools import permutations

def m_lists(n, m):
    l = [x for x in range(1, n+1)]

    s = permutations(l, m)

    for i in s:
        print(*list(i))



if __name__ == '__main__':
    n, m = map(int, input().split())

    m_lists(n, m)