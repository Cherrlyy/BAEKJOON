def sum(a, b):
    return a+b

def minus(a, b):
    return a-b

def multiple(a, b):
    return a*b

def quotient(a,b):
    if b != 0:
        return a//b

def remainder(a, b):
    return a%b

if __name__ == '__main__':
    tmpList = list(map(int, input().split()))

    print(sum(tmpList[0], tmpList[1]))
    print(minus(tmpList[0], tmpList[1]))
    print(multiple(tmpList[0], tmpList[1]))
    print(quotient(tmpList[0], tmpList[1]))
    print(remainder(tmpList[0], tmpList[1]))

