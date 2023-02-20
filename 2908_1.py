def compare_nums(l):
    for i in reversed(range(3)):
        if int(l[0][i]) > int(l[1][i]) :
            return l[0][::-1]
        elif int(l[0][i]) < int(l[1][i]) :
            return l[1][::-1]


if __name__ == '__main__':
    nums = input().split()
    print(compare_nums(nums))