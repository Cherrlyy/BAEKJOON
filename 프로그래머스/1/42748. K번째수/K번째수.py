def return_answer(l, k):
    new = [l[0]]
    for i in range(1, len(l)):
        for e in range(len(new)):
            if l[i] <= new[e]:
                new.insert(e, l[i])
                break
        else:
            new.append(l[i])
    return new[k-1]
                
    

def solution(array, commands):
    answer = []
    for c in commands:
        a, b, k = c[0], c[1], c[2]
        num = return_answer(array[a-1:b], k)
        answer.append(num)
    return answer