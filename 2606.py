def count_infect():
    cnt = -1
    while need_visit:
        current = need_visit[0]
        cnt+=1
        need_visit.remove(current)

        for e in graph[current]:
            if not visited[e] and e not in graph:
                need_visit.append(e)
                visited[e] = True

    return cnt


if __name__ == '__main__':
    n = int(input())
    v = int(input())
    need_visit = [1]
    visited = [False]*(n+1)
    visited[1] = True
    graph = [[] for i in range(n+1)]
    for _ in range(v):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(count_infect())