from itertools import combinations

def solution(numbers, target):
    n = (sum(numbers) - target)//2
    l = []
    for i in range(1, len(numbers)):
        l.extend(list(filter(lambda x: sum(x) == n, combinations(numbers, i))))

    answer = len(l)
    return answer