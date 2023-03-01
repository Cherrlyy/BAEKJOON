def loc_num(x1, y1, r1, x2, y2, r2):
    squared_dist = (x2-x1)**2 + (y2-y1)**2
    squared_r_sum = (r1+r2)**2
    squared_r_diff = (r2-r1)**2

    if squared_dist == 0:
        if r1 == r2:
            return -1
        else:
            return 0

    else:
        if squared_r_diff < squared_dist and squared_r_sum > squared_dist:
            return 2
        elif squared_r_sum == squared_dist or squared_r_diff == squared_dist:
            return 1
        elif squared_r_diff > squared_dist or squared_r_sum < squared_dist:
            return 0


if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        x1, y1, r1, x2, y2, r2 = map(int, input().split())
        print(loc_num(x1, y1, r1, x2, y2, r2))