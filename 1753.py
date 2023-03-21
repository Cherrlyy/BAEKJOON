from collections import deque

def min_dist(v, k):
    q = deque([k])
    dists = {point: 0 for point in range(v+1)}

    while q:
        visit_point = q.popleft()
        for j in lines:
            if j[0] == visit_point:
                if dists[j[1]] == 0:
                    q.append(j[1])
                    dists[j[1]] = dists[visit_point] + j[2]


    for i in range(1, len(dists)):

        if not i == k and dists[i] == 0:
            print('INF')
        else:
            print(dists[i])


if __name__ == '__main__':
    v, e = list(map(int, input().split()))
    k = int(input()) #시작점
    lines = []

    for i in range(e):
        lines.append(list(map(int, input().split())))
    min_dist(v, k)