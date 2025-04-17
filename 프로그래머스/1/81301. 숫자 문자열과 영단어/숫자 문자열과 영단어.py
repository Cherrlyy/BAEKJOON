def solution(s):
    alph = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
    for a in alph.keys():
        if a in s:
            s = s.replace(a, str(alph[a]))
    answer = int(s)
    return answer