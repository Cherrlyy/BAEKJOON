from collections import deque

def solution(n, computers):
    answer = 0
    visited = [0]*(n)
    
    
    while 0 in visited:
        d = deque()
        d.append(visited.index(0))
        while d:
            current = d.popleft()
            visited[current] = 1
            for i in range(n):
                if computers[current][i] == 1 and visited[i] == 0:
                    d.append(i)
        answer += 1
    return answer