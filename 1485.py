from itertools import combinations

def make_square(l):
    comb = combinations(l, 2)

    for c in comb:


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        vertexs = []
        for j in range(4):
            vertexs.append(list(map(int, input())))
        print(make_square(vertexs))