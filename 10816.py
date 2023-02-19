from collections import Counter


def is_in(card_set, find_set):
    ans = []s
    counter = Counter(card_set)
    for find_num in find_set:
        ans.append(counter[find_num])

    return ans


if __name__ == "__main__":
     n = int(input())
     card_set = list(map(int, input().split()))
     m = input()
     find_set = list(map(int, input().split()))

     print(*is_in(card_set, find_set))
