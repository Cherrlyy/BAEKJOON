import math

def cases_of_bridge(l):
    n, m = l[0], l[1]
    return math.comb(m, n)


if __name__ == "__main__":
     n = int(input())

     for i in range(n):
         print(cases_of_bridge(list(map(int, input().split()))))
