import sys
sys.setrecursionlimit(1000001)

def print_primenums(a, b):
    for i in range(a, b+1):
        if is_prime(i, 2):
            print(i)


def is_prime(n, m):
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
    a, b = map(int, input().split())
    print_primenums(a, b)
