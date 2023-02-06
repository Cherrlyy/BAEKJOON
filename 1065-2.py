def arithmeticSeauence(n):
    ans = 0
    for i in range(1, n+1):
        digits = [int(x) for x in str(i)]
        if len(digits) > 2:
            if isDifference(digits):
                continue
        ans = ans + 1
    return ans

def isDifference(digits):
    tmp = set()
    for j in range(len(digits) - 1):
        tmp.add(digits[j + 1] - digits[j])
    if len(tmp) == 1:
        return False
    return True

if __name__ == '__main__':
    n = int(input())
    print(arithmeticSeauence(n))