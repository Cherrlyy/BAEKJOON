import math


def movie_title(n):
    # tmp = 0
    # i = 0
    # while True:
    #     string_i = str(i)
    #
    #
    #     i+=1

    tmp = 3
    while True:
        if n < 2:
            break
        elif n < math.comb(tmp, 1) * 9^(n-3):
            break



if __name__ == "__main__":
     n = int(input())



     # 3자리수 : 666 -> 0C0
     # 4자리수 : n666 666n -> 2C1 * 9
     # 5자리수 : nn666 n666n 666nn -> 3c1 * 9*9
     # n자리수  : (n-2)C1 * 9^(n-3)