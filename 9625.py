def a(str, n):
    if n == 0:
        return str
    tmp = ''
    for i in range(len(str)):
        if str[i] == 'B':
            tmp+='BA'
        else:
            tmp+='B'
    n-=1
    return a(tmp, n)


n = int(input())
ans = a('A', n)
print(ans.count('A'), end=' ')
print(ans.count('B'))
