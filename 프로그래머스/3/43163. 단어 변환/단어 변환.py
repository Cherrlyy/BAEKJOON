from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    need_visit = set(words)
    d = deque()
    d.append((begin, 0))

    while d:
        current, step = d.popleft()
        if current == target:
            return step

        for word in need_visit:
            cnt = 0
            for i in range(len(current)):
                if current[i] != word[i]:
                    cnt+=1
            if cnt == 1:
                d.append((word, step+1))