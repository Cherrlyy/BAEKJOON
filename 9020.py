def goldbach(n):

    i = n//2
    while True:
        if is_prime(i) and is_prime(n-i):
            return [i, n-i]
        i-=1

    # for i in range(2, n//2+1):
    #     if is_prime(i) and is_prime(n-i):
    #         ans = [i, n-i]
    #
    # return ans



def is_prime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        print(*goldbach(n))