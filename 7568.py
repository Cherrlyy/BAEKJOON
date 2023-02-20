

def order_size(x, y, pre_tmp):
    tmp = 1
    # 요소가 0개이면 앞에 비교할 게 없기 때문에 일단 append
    if len(size_list) == 0:
        size_list.append([x, y])

    else:
        for i in range(len(size_list)):
            if size_list[i][0] > x and size_list[i][1] > y:
                continue
            elif size_list[i][0] > x or size_list[i][1] > y:
                size_list.insert(i+1, [x, y])
                tmp+=1
            else:
                size_list.insert(i, [x, y])

    print('pre :', pre_tmp)
    print('tmp: ', tmp)
    if pre_tmp < tmp:
        return tmp

    else:
        l1.append(pre_tmp)
        return tmp



    # 입력 받을 때마다 리스트의 처음부터 순서대로 비교해 집어넣기 -> 매번 정렬 (삽입정렬)


if __name__ == "__main__":
    n = int(input())
    size_list = []
    l1 = []

    pre_tmp = 1

    for i in range(n):
        x, y = map(int, input().split())
        pre_tmp = order_size(x, y, pre_tmp)
        # print(pre_tmp)

        # tmp_list.append([x, y])

    print(l1)


        # 삽입정렬 후 순서 어떻게 출력?
        # 1 2 2 4 4 4 7


    # x, y 입력 -> 앞에서부터 훑으면서
    # 앞보다 x, y 다 작으면 뒤로 / 앞(i)보다 x, y 둘 다 크면 그 위치(i)에 삽입
    # 앞(i)보다 x 또는 y 중 하나만 크면 그 뒤 위치(i+1)에 삽입 후 tmp += 1
    # 다 돌았는데 다 통과했으면(모든 앞의 요소보다 x, y 모두 작음) 맨 마지막에 넣기

    # tmp 는 연속된 동일 등수의 개수
    # 88 186 (tmp 1) / 55, 185 (tmp 1) / 58, 183 (tmp 2) / 60 175 (tmp 3) / 46 155 (tmp 1)
    # 앞 요소의 tmp 항상 갖고 있고 다음 거가 더 크면 tmp 바꾸기 / 다음 거가 앞에 거보다 작거나 같으면 앞에 거 저장
    # 앞의 요소(i번째) 저장(tmp_people) 후 앞보다 x, y 중 하나만 클 경우 tmp+=1
    # 아닐 경우 tmp 저장 후 tmp 리셋