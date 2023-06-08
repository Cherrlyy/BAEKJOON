def set_card(num_dep):
    if num_dep == k:
        ans.append(num.copy())
        return
    else:
        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                num[num_dep] = cards[i]
                set_card(num_dep+1)
                visited[i] = False
        return


n = int(input())
k = int(input())
cards = []
for _ in range(n):
    cards.append(int(input()))
visited = [False for _ in range(n)]
ans = []
num = [0]*k
set_card(0)
print(len(ans))
print(ans)
