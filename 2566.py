

def print_sol(l):
    maxs = []
    idx_of_maxs = []
    for i in range(len(l)):
        max_of_l = max(l[i])
        maxs.append(max_of_l)
        idx_of_maxs.append(l[i].index(max_of_l))
    m = max(maxs)
    print(m)
    idx = maxs.index(m)
    print(idx+1, idx_of_maxs[idx]+1)


if __name__ == '__main__':
    grid = [list(map(int, input().split())) for i in range(0, 9)]

    print_sol(grid)




