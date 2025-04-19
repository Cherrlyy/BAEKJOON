def m_n(depth, idx):
    if depth >= m:
        arr_l.append(arr.copy())
        return
    else:
        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                arr[depth] = l[i]
                m_n(depth + 1, i)
                visited[i] = False
        return

if __name__ == "__main__":
    n, m = map(int, input().split())
    l = [i for i in range(1, n+1)]
    visited = [False]*n
    arr_l = []
    arr = [0]*m
    m_n(0, 0)

    for e in arr_l:
        print(*e, sep=' ')