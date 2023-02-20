from collections import Counter
def num_of_nums(l):
    new = multiply(l)
    count = Counter(str(new))

    for i in range(10):
        if str(i) in count:
            print(count[str(i)])
        else:
            print(0)

def multiply(l):
    tmp = 1
    for i in l:
        tmp*=i
    return tmp

if __name__ == '__main__':
    nums = []
    for i in range(3):
        nums.append(int(input()))
    num_of_nums(nums)