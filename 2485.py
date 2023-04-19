def street_trees():
    a = trees[1] - trees[0]
    # for i in range(2, len(trees)):
    #
    #     b = min(a, (trees[i] - trees[i-1]))
    #     a = max(a, (trees[i] - trees[i-1]))
    #
    #
    #     while (b != 0):
    #         r = a % b
    #         a = b
    #         b = r


    a = trees[1] - trees[0]
    for i in range(2, len(trees)):


        b = trees[i] - trees[i-1]
        print('2:', a, b)

        while (b != 0):
            r = a % b
            a = b
            b = r
            print(r)



    # ans = 0
    # for i in range(trees[0], trees[-1]+1, a):
    #     if i not in trees:
    #         ans+=1

    return (trees[-1] - trees[0])//a - (n-1)



if __name__ == "__main__":
    n = int(input())
    trees = []
    for i in range(n):
        trees.append(int(input()))

    print(street_trees())