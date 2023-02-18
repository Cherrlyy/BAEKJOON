def is_in(card_set, find_set):
    ans = []
    for num in find_set:
        if num in card_set:
            ans.append(1)
        else:
            ans.append(0)
    return ans


if __name__ == "__main__":
     n = int(input())
     card_set = set(map(int, input().split()))
     m = input()
     find_set = map(int, input().split())

     print(*is_in(card_set, find_set))