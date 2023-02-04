from collections import deque

def lastCard(cards):
    while len(cards) > 0:
        print(str(cards.popleft()), end=' ')
        if len(cards) != 0:
            cards.append(cards.popleft())



if __name__ == '__main__':
    numCards = int(input())
    cards = deque([x for x in range(1, numCards+1)])

    lastCard(cards)