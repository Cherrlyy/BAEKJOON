def get_diff_min(depth, idx):
    if depth == n//2:
        diff = 0
        for i in range(len(team_start)):
            for j in range(i+1, len(team_start)):
                diff += s[team_start[i]][team_start[j]]
                diff += s[team_start[j]][team_start[i]]

        team_link = [e for e in l if e not in set(team_start)]
        for i in range(len(team_link)):
            for j in range(i+1, len(team_link)):
                diff -= s[team_link[i]][team_link[j]]
                diff -= s[team_link[j]][team_link[i]]

        m.append(abs(diff))
        return

    else:
        for i in range(idx, n):
            if visited[i] == False:
                visited[i] = True
                team_start[depth] = l[i]
                get_diff_min(depth+1, i)
                visited[i] = False
        return

if __name__ == "__main__":
    n = int(input())
    s = []
    l = [i for i in range(n)]
    visited = [False]*n
    team_start = [0]*(n//2)
    for _ in range(n):
        s.append(list(map(int, input().split())))

    m = []


    get_diff_min(0, 0)
    print(min(m))