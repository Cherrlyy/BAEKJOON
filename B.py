#indexError
# n < k
# n < m (누적) -> 끝내기 (i가 len(n)이랑 같을때 m은 남아있음)
# m < n (누적) -> n의 길이까지 꼐속 하나씩 늘려가면서 ans에 추가
#

def sol(n_str, m_str, i, j, k):
    print('시작')
    m_str = m_str[i-1:j]
    if k == 0:
        find_same(n_str, m_str, '', k, '', [])
    else:
        part_str = m_str[:k]
        n_str = n_str[n_str.find(part_str):]
        find_same(n_str, m_str, part_str, k, part_str, [])


def find_same(n_str, m_str, part_str, idx, tmp, ans):
    tmp = tmp
    idx = idx
    part_str = part_str
    print('n', n_str)
    print('tmp', tmp)
    if tmp != '':
        ans.append(tmp)
    print(ans)

    if len(n_str) < k or len(n_str) == idx:
        return len(ans)
        # 연속 중복 갯수가 k 보다 작을 땐 ans에 누적
        # k랑 같으면 다음 거 비교
        #

    if idx == 0 and n_str[idx] == m_str[idx]:
        print('1번 케이스')
        print('part:', part_str)
        if part_str == '':
            find_same(n_str[1:], m_str, part_str, idx, part_str, ans)
        t = n_str.find(part_str)
        if t < 0:
            return len(ans)
        find_same(n_str[n_str.find(part_str):], m_str, part_str ,idx, part_str, ans)

    elif n_str[idx] != m_str[idx] or (idx != 0 and n_str[idx] == m_str[idx]):
        print('2, 3번')
        if len(m_str)-1 != idx:
            tmp += n_str[idx]
            print('2번 케이스')

            find_same(n_str, m_str, part_str , idx+1 , tmp, ans)
        elif len(m_str)-1 == idx:
            print('3번 케이스')

            for i in range(len(n_str)):
                tmp += n_str[idx]
                ans.append(tmp)
                if part_str == '':
                    find_same(n_str[1:], m_str, part_str, idx, part_str, ans)
                find_same(n_str[n_str.find(part_str):], m_str, part_str, idx, part_str, ans)

    return
    #     다를 경우 해당 tmp 저장 / 다음 요소 비교



#m_str 길이가 짧을 경우 -> 하나씩 끝까지 모든 경우의 수 / 다시 n_str 자름
#n_str의 길이가 짧을 경우
#전부 다 돌은 경우 1. m_str이 짧아서 돈 경우 2.그냥 다 체크해서 없을 경우
    #     if len(tmp) >= k and tmp != '':
    #         l.append(tmp) # a vs a // m_str이 먼저 끝날 경ㅇ
    #
    #         if i == len(n_str) and i >= len(m_str):
    #             n_str = n_str[len(m_str):]
    #             n_str = n_str[n_str.find(part_str):]
    #             tmp = ''
    #             i = 0
    #             continue
    #
    #         if i == len(n_str):
    #             break
    #         if i >= len(m_str):
    #             tmp+= n_str[i]
    #         elif n_str[i] == m_str[i]:
    #             n_str = n_str[k:]
    #             n_str = n_str[n_str.find(part_str):]
    #             tmp = ''
    #             i = 0
    #             continue
    #         else:
    #             tmp += n_str[i]
    #
    #     else:
    #         while len()
    #         if n_str[i] == part_str[i]:
    #             tmp += n_str[i]
    #     i+= 1
    #
    # print(len(l))

# 기존 문자열에서 찾는 부분 문자열이 있는지 i로 확인
# 갯수를 채웠다면 그 다음은 비교문자열의 그 다음번째와 기존 문자열 다음 거 확인
# 그 다음 게 없으면(마지막 요소였으면) 오류나므로 갯수 채우면 끝내기

# ask / a
# anana

#

if __name__ == '__main__':
    tk = 'ajd'

    n, m, q = map(int, input().split())

    n_str = input()
    m_str = input()

    for i in range(q):
        i, j, k = map(int, input().split())
        sol(n_str, m_str, i, j, k)


#indexError
# n < k
# n < m (누적)
# m < n (누적)
#