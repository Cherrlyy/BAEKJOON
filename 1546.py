def avg_scores(l):
    new = list(map(new_score, l, [max(l) for i in range(len(l))]))
    return sum(new)/len(new)


def new_score(score, m):
    return score/m*100



if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    print(avg_scores(scores))