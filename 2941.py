
ans = []
dict_alpha = set(['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='])


def revise_alpha(str, ans):
    if len(str) == 0:
        return ans

    for i in range(2, 4):
        tmp = str[0:i]
        if tmp in dict_alpha:
            ans.append(tmp)
            return revise_alpha(str[i:], ans)
    tmp = str[0]
    ans.append(tmp)
    return revise_alpha(str[1:], ans)


if __name__ == '__main__' :
    str = input()
    print(len(revise_alpha(str, ans)))
