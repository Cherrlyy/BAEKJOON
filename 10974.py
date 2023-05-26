# def num_permutation(idx1, idx2, perm):
#     if idx1 == 0:
#         return 0
#     if idx1 == n-1:
#         print(*perm, sep=' ')
#     if idx2 == n-1:
#         return num_permutation(idx1-1, idx2-1, perm)
#
#     return num_permutation(idx2+1, perm)
#     tmp = perm[:idx] + sorted(perm[idx:])
#     print(*tmp, sep=' ')
#
#     return  num_permutation()

if __name__ == "__main__":
    n = int(input())
    l = [i for i in range(1, n+1)]

    #idx1 : 바뀌는 위치 / idx2 : 내부에서 바뀌는 위치
    # print(num_permutation(0, n-1, l),l)

    # idx 두개 바뀌는 곳에 대해서 재귀 돌림
    def a(idx, perm_l):
        # print(idx)
        print('----------------------------')
        print('l:', l)
        print('idx', idx, perm_l)
        for i in range(idx+1, n-idx+1):
            #i는 숫자임 고정되는 부분 반복될 부분임
            # t =  #바뀌는 부분
            # print(t)
            # print(t.index(i))
            print('뺄 숫자(고정 숫자)', i)
            t = l[idx:]
            print('t', t)
            t.remove(i)
            perm_l = t
            print('내부에서 뒤바뀔 순열', perm_l)

            # print(perm_l)
            # print(type(perm_l))
            # print(type([i]))
            # print(type(a(idx+1, perm_l[idx+1:])))
            tmp = [i] + a(idx+1, perm_l[1:])
            print('a', a(idx+1, perm_l[1:]))
            print(tmp)
            return tmp

        else:
            return []



    print(a(0, l))