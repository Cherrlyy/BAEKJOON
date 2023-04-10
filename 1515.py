def follow_num(n):
    # 변수 int 두개로 하나는 현재 10 이상의 자릿수 체크
    # 하나는 일의자릿수 체크
    # 숫자 증가 -> 10 이내 존재 : 자릿수 늘릴 필요 x
    # 증가 x : 현재 십의자릿수 체크 -> 다음숫자와 자릿수 동일하면 십의자릿수로 생각하고 다음 숫자 체크

    # 자릿수 다르면 일의자릿수로 체크라기
    # 이때 십의자릿수 증가해야 함
    n1, n2 = 0, 0
    pre = int(n[0])
    for i in range(1, len(n)):
        print('stt', n1, n[i])
        tmp = int(n[i])
        print(tmp)
        if tmp > pre:
            pre = tmp
            continue
        else:
            print('!', n1)
            if tmp == n1 and n1 != 0:
                print('!!!')
                print(tmp)
                pre = tmp

                continue
            else:
                print('!!')
                n1+=1
                if n1 == tmp:
                    pre = 0
                else:
                    pre = tmp



    print(n1, pre)

if __name__ == '__main__':
    n = input()
    print(follow_num(n))