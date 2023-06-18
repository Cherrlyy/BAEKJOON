def find_city():
    need_visited = [start]
    visited = [-1]*(n+1)

    visited[start] = 0
    while need_visited:
        current = need_visited[0]
        need_visited.remove(current)
        if visited[current] == k:
            cities.append(current)
            continue
        for e in graph[current]:
            if visited[e] == -1:
                visited[e] = visited[current] + 1
                need_visited.append(e)



if __name__ == '__main__':
    n, m, k, start = map(int, input().split())
    graph = [[] for i in range(n+1)]
    cities = []
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
    find_city()

    if len(cities) == 0:
        print(-1)
    else:
        cities.sort()
        print(*cities, sep='\n')


# bfs로 풀어야 좋은 이유: 그래프로 이어져있으며 같은 거리에서 판단해야 하는 문제이므로,
# 깊이별로 판단이 가능한 bfs 알고리즘이 유리하다.