def compare_nums(l):
    for i in range(len(l)):
        l[i] = list(l[i])
        l[i].reverse()
        l[i] = int(''.join(l[i]))
    return max(l)



if __name__ == '__main__':
    nums = input().split()
    print(compare_nums(nums))