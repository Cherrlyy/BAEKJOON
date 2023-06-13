def make_a_k():
    need_visit = [a]
    graph[a] = 0
    while need_visit:
        current = need_visit[0]
        if current == k:
            return graph[current]
        need_visit.remove(current)

        if current+1 <= k and graph[current+1] == -1:
            graph[current+1] = graph[current]+1
            need_visit.append(current+1)

        if current*2 <= k and graph[current*2] == -1:
            graph[current*2] = graph[current]+1
            need_visit.append(current*2)



if __name__ == '__main__':
    a, k = map(int, input().split())

    graph = [-1 for i in range(k+1)]

    print(make_a_k())