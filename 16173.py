import sys
sys.setrecursionlimit(10**6)

def jjelly(x_square, y_square):
    if x_square > n-1 or y_square > n-1 or visited[x_square][y_square] == 1:
        return
    if l[x_square][y_square] == -1:
        visited[x_square][y_square] = 1
        return

    visited[x_square][y_square] = 1
    jjelly(x_square, y_square+l[x_square][y_square])
    jjelly(x_square+l[x_square][y_square], y_square)


if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    visited = [[0]*n for _ in range(n)]
    jjelly(0, 0)
    if visited[-1][-1] == 1:
        print('HaruHaru')
    else:
        print('Hing')

# 예외처리와 재귀 부분 나눠 처리한 건 good.
# 그러나 백트래킹에서 visited 사용하는 연결이 부족했음.
# 또 정확히 예외가 어떤부분에 생기는지 깊게 생각해보는 연습해야 할 듯함.