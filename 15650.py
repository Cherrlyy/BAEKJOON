def m_n(depth):
    if depth >= m:
        arr_l.append(arr.copy())
        return
    else:
        for i in range(n):
            if not visited[i]:
                if l[i] > arr[depth-1]:
                    visited[i] = True
                    arr[depth] = l[i]
                    m_n(depth+1)
                visited[i] = False
        return

if __name__ == "__main__":
    n, m = map(int, input().split())
    l = [i for i in range(1, n+1)]
    visited = [False]*n
    arr_l = []
    arr = [0]*m
    m_n(0)

    for e in arr_l:
        print(*e, sep=' ')