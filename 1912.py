import copy


def sequence_sum(n, l):
    a = copy.deepcopy(l)
    for i in range(1, n):
        a[i] = max(a[i-1]+l[i], a[i])


    return m

if __name__ == '__main__':
    n = int(input())
    l = list(map(int, input().split()))

    print(sequence_sum(n, l))


