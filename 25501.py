def isPalindrome(s, n):
    n += 1
    if len(s) <= 1:
        return [1, n]

    if s[0] == s[-1]:
        return isPalindrome(s[1:-1], n)

    return [0, n]


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        str = input()
        print(*isPalindrome(str, 0))