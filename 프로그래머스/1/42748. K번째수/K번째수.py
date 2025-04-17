def solution(array, commands):
    answer = []
    for c in commands:
        a, b, k = c[0], c[1], c[2]
        num = sorted(array[a-1:b])[k-1]
        answer.append(num)

    return answer