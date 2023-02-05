def compare(a, b):
    if a > b:
        return('>')
    elif a < b:
        return('<')
    else:
        return('==')


if __name__ == '__main__':
    a, b = list(map(int, input().split()))

    print(compare(a, b))