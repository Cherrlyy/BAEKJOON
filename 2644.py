def famaily_num(now):
    # visited[now] = True
    flag = False

    #분개
    for i in range(len(rels)):
        if rels[i][0] == now:
            flag = True
            famaily_num(rels[i][1])
    # 끝까지 갔으나 못 찾았을 경우 return
    if not flag and now not in search:
        visited[now] = True
        return

if __name__ == '__main__':
    n = int(input())
    search = list(map(int, input().split()))
    m = int(input())

    # idx = 1부터 사용
    visited = [False]*(n+1)

    rel_visited = [False]*(m)
    rels = []
    for _ in range(m):
        rels.append(list(map(int, input().split())))


    while (not all(rel_visited)) and len(search) != 0:
        famaily_num(rels[rel_visited.index(False)][0])
        print(visited)
        if visited[search[0]] and visited[search[1]]:
            print(visited.count(True))
            break
        elif visited[search[0]] & visited[search[1]] == False:
            print(-1)
            break
        else:
            visited = [False]*(n+1)


