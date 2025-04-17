from collections import deque


def solution(maps):
    visited_cnt = [[0]*len(maps[0]) for _ in range(len(maps))]
    need_visit = deque([(0, 0)])
    visited_cnt[0][0] = 1

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    while need_visit:
        current = need_visit.popleft()
        if current[0] == len(maps)-1 and current[1] == len(maps[0])-1:
            break 

        for i in range(len(dx)):
            x = current[0]+dx[i]
            y = current[1]+dy[i]

            if x > len(maps)-1 or x < 0 or y > len(maps[0])-1 or y < 0:
                continue
            if maps[x][y] == 0:
                continue
            if visited_cnt[x][y] != 0:
                continue
            visited_cnt[x][y] = visited_cnt[current[0]][current[1]] + 1
            need_visit.append((x, y))

    answer = visited_cnt[len(maps)-1][len(maps[0])-1] if visited_cnt[len(maps)-1][len(maps[0])-1] != 0 else -1

    return answer