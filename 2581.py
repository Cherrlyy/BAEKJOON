import sys
sys.setrecursionlimit(10000)

def print_primenums(a, b):
    l = []
    for i in range(a, b+1):
        if is_prime(i, 2):
            l.append(i)
    if len(l) == 0:
        print(-1)
    else:
        print(sum(l))
        print(min(l))
# n % m 확인
# m : n 또는 1 패스 : 2~n-1번째까지
def is_prime(n, m):
    # print("n, m: ",n, m)
    if n == 1 or n == 2:
        return False
    else:
        if m == n:
            return True
        elif n % m == 0:
            return False
        else:
            return is_prime(n, m+1)

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print_primenums(a, b)

# 이중for문 -> 최소 O(nlogn)의 시간복잡도로 어떻게 줄이지?