from collections import deque

def josephus(n, k):
    peoples = deque([x for x in range(1, n+1)])
    print('<', end='')
    while len(peoples) != 0:
        peoples.rotate(-(k-1))
        if len(peoples) == 1:
            print(peoples.popleft(), end='>')
            continue

        print(peoples.popleft(), end=', ')


if __name__ == '__main__':
    n, k = list(map(int, input().split()))

    josephus(n, k)