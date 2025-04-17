def solution(strings, n): 
    t = [(s, s[n]) for s in strings]
    t = sorted(t, key=lambda x:(x[1], x[0]))
    answer = map(lambda x:x[0], t)
    return list(answer)