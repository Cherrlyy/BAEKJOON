def check(n):
    ans = []
    for i in range(n):
        str =input()
        if seqeunce(str):

            ans.append(str)
    return len(ans)


def seqeunce(str):
    alpha = set()
    tmp = 0
    for i in range(len(str)):
        if str[i] == tmp:
            continue
        else:
            if str[i] in alpha:
                return False
            else:
                alpha.add(str[i])
                tmp = str[i]
    return True


if __name__ == '__main__':
    n = int(input())

    print(check(n))
