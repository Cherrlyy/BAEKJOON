def depart_sum(n):
    string_n = str(n)
    for i in range(n - len(string_n)*9, n):
        if i < 0:
            continue
        tmp = i
        for j in str(i):
            tmp += int(j)
        if tmp == n:
            return i

    return 0

if __name__ == "__main__":
    n = int(input())
    print(depart_sum(n))