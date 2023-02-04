from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write



def lastCard(queue):
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())
    print(str(queue[0]))


if __name__ == '__main__':
    numCards = int(input())
    cards = deque([x for x in range(1, numCards+1)])

    lastCard(cards)

