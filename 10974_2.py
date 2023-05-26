def permutation(level):
    if level >= n:
        arr_l.append(arr.copy())

    else:
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                arr[level] = l[i]
                permutation(level + 1)
                # 끝나고 돌아옴
                visited[i] = False




n = int(input())
l = [i for i in range(1, n + 1)]
print(l)
visited = [False] * n
arr = [0] * n
arr_l = []
level = 0
permutation(0)
print(arr_l)
