import re
def reverse(str):
    stack = []
    queue = []
    open = False
    for s in str:
        print(s)
        # print(stack)
        # print(queue)
        # print(s)
        if s == '<':
            open = True
            # print(s)
        elif s == '>':
            open = False
            while len(queue) != 0:
                queue.pop(0)
            # print(s)
        if open:
            queue.append(s)
        elif not open:
            if s == ' ':
                while len(stack) != 0:
                    stack.pop()
                # stack 내용 전부 pop
                # print(s)
            else:
                stack.append(s)
                # stack에 add 하기





        # if s == ' ':
        #     # print('empty', s)
        #     while len(stack) != 0:
        #         print(stack.pop(), end='')
        #     print(s, end='')
        # if s == '<':
        #     # print('open tag', s)
        #     while len(stack) != 0:
        #         print(stack.pop(), end='')
        #     # print(s, end='')
        #     open = True
        #     # print(s, end='')
        # if s == '>':
        #     # print('close tag', s)
        #     open = False
        #     # print()
        #     # print('queue')
        #     # print(*queue)
        #     while len(queue) != 0:
        #         print(queue.pop(0), end='')
        #     print(s, end='')
        #
        # elif open:
        #     # print('open', s)
        #     queue.append(s)
        # elif not open:
        #     # print('close', s)
        #     stack.append(s)



if __name__ == '__main__':
    str = input()

    reverse(str)


    # 구분 후 단어는 뒤집기 태그는 뗐다가 출력 시 붙이기

    # 한글자씩 확인하며 stack에 넣기.
    # 공백 문자 올 시 모두 pop후 다음문자부터 다시 stack
    # 여는 괄호 올 시 닫는 괄호 나타날 때까지 그냥 힙에 넣기
    # 닫는 괄호 나타날 시 모두 pop 후 다음 문자부터 다시 stack
    # open일 때 띄쓰 / 문자
    # close일 때 띄쓰 / 문자
    # 경우 나워서 다시 해보기