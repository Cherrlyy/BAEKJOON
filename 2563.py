from itertools import permutations

def get_area(n, start_papers):



    # x나 y가 10이상씩 간격을 가질 것.
    # 모든 경우에 대해 10 이상 차이인지 따지기: 종이 3장이라 경우의수 3임
    # but, 종이 개수 바뀔 수도 있으므로 콤비네이션 구하기 (종이수x(종이수-1)/2!)
    # 10보다  작을 경우 x: 10-차이 y: 10- 차이 만큼 겹침
    # 색종이 너비 다 더하기 - 겹치는 부분


if __name__ == '__main__':
    n = int(input()) # 색종이 수

    area = n * 10 * 10

    rl = permutations(starts)

    


    # 종이 시작 위치 입력 받기
    # 종이 전부 더하기
    # 겹친 부분 지우기
    # x 끼리는 10 이상 차이
    # y 끼리는 10 이상 차이
    # 둘 중 하나만 만족하면 됨
    10 - (y 시작점 차이) * 10 - (x 시작점 차이 )
