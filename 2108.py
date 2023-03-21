from collections import defaultdict


def avg_sum(n, nums):
    return round(sum(nums)/n)

def mid(n, nums):
    return nums[n//2]

def most_freq(n, nums):
    dict = {x:0 for x in nums}
    for n in nums:
        dict[n] = dict[n] + 1

    m = max(dict.values())
    m_key = [k for k,v in dict.items() if v == m]

    if len(m_key) == 1:
        return m_key[0]
    m_key.sort()
    return m_key[1]

def m_range(n, nums):
    return (nums[n-1] - nums[0])


if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    nums.sort()

    print(avg_sum(n, nums))
    print(mid(n, nums))
    print(most_freq(n, nums))
    print(m_range(n, nums))



