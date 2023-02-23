# def make_one(n):
#     print(n)
#
#     if n in cache:
#         return cache[n]
#
#     if n in (1, 2, 3):
#         cache[n] = 1
#         return cache[n]
#
#     if n % 3 == 0:
#         cache[n] = 1 + make_one(n//3)
#         return cache[n]
#     elif n % 2 == 0:
#         cache[n] = 1 + make_one(n//2)
#         return cache[n]
#     cache[n] = 1 + make_one(n-1)
#     return cache[n]


def make_one(n):
    cache = dict()
    cache[1] = 0
    for i in range(2, n+1):
        if i in (2, 3):
            cache[i] = 1
            continue

        tmp = []
        if i % 3 == 0:
            tmp.append(cache[i//3])
        if i % 2 == 0:
            tmp.append(cache[i//2])
        tmp.append(cache[i-1])

        cache[i] = 1 + min(tmp)

    return cache[n]



if __name__ == '__main__':
    n = int(input())

    print(make_one(n))

# BFS로도 풀이해볼 것