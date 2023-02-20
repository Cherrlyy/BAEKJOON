def get_area(n, start_papers):
    a, b = 10, 10
    overlap = 0
    for i in range(n):
        for j in range(i+1, n):
            diff_x = abs(start_papers[i][0] - start_papers[j][0])
            diff_y = abs(start_papers[i][1] - start_papers[j][1])
            if diff_x < 10 and diff_y < 10:
                overlap = (10 - diff_x) * (10 - diff_y)

    ans = n*a*b - overlap
    return ans


    # x나 y가 10이상씩 간격을 가질 것.
    # 모든 경우에 대해 10 이상 차이인지 따지기: 종이 3장이라 경우의수 3임
    # but, 종이 개수 바뀔 수도 있으므로 콤비네이션 구하기 (종이수x(종이수-1)/2!)
    # 10보다  작을 경우 x: 10-차이 y: 10- 차이 만큼 겹침
    # 색종이 너비 다 더하기 - 겹치는 부분


if __name__ == '__main__':
    n = int(input()) # 색종이 수


    # 종이 시작 위치 입력 받기
    start_papers = [list(map(int, input().split())) for i in range(n)]
    print(get_area(n, start_papers))