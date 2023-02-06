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
    diff = digits[1] - digits[0]
    for j in range(len(digits) - 1):
        if j == 0:
            continue
        else:
            if digits[j + 1] - digits[j] != diff:
                return True
    return False

if __name__ == '__main__':
    n = int(input())
    print(arithmeticSeauence(n))