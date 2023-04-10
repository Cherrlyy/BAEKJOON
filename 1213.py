from collections import Counter

def make_palindrome(s):
    # 받은 문자열 길이가 홀수면 홀수 개로 한 개는 가운데에 기준 / 나머지는 모두 짝으로 존재
    # 짝수면 모두 짝으로 존재해야 함
    # 이게 안 맞으면 문자열 출력

    # 사전순으로 갯수/2로 배열


    # 딕셔너리 돌면서 짝수 개면 넘기기
    # 홀수 개이면
    # 홀수 개인데 이미 홀수 개인 알파벳이 있을 때
    # 홀수 개인데 홀수 개인 다른 알파벳이 없을 때

    # 알파벳 순으로 출력
    # 홀수 개가 없을 때 => 그냥 반만 출력 후 뒤집어 붙이기
    # 홀수 개가 있을 때 => 반만 출력 후 하나는 가운데 붙이고
    count = Counter(s)
    count = dict(sorted(count.items()))
    sym_point = None
    ans = ""
    # print(count)
    for key in count:
        # print(key)
        if not count[key] % 2 == 0:
            # print(key)
            if sym_point != None:
                return "I\'m Sorry Hansoo"
            else:
                sym_point = key
                count[key] -= 1

    # print(count)
    for key in count:
        # print(count[key]//2)
        for i in range(count[key]//2):
            # print(i)
            ans += key

    if sym_point != None:
        return ans + sym_point + ans[::-1]
    else:

        return ans + ans[::-1]



if __name__ == '__main__':
    s = input()
    print(make_palindrome(s))
