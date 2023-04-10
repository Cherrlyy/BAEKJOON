def sym_subtraction(l1, l2):
    return len(l1 - l2) + len(l2 - l1)

if __name__ == '__main__':
    n, m = map(int, input().split())

    l1 = set(map(int, input().split()))
    l2 = set(map(int, input().split()))

    print(sym_subtraction(l1, l2))