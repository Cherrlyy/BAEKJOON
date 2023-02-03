class Node:
    def __init__(self, item):
        self.item = item


    def setNext(self, next):
        self.next = next

# n개의 원소를 지닌 링크드리스트 만들기

class CircleLinkedList:
    ans = []
    def __init__(self, n):
        self.head = None
        self.tail = None
        self.count = n
        self.setCircleLinkedList(count)

    def setCircleLinkedList(self, n):
        pre = None
        for i in range(n):
            node = Node(i+1)
            if self.head is None:
                self.head = node
            self.tail = node
            if pre is not None:
                pre.next = node
            pre = node
        self.tail.next = self.head


    # tail이 꼭 필요한지?


    def pop(self, node):
        self.ans.append(node.next.item)
        node.next = node.next.next
        self.count = self.count - 1

    # tail도 처리해주어야 하나?

# n번째마다 삭제
    def repeatDelete(self, n):
        node = self.head
        num = 0
        while self.count != 0:
            num = num + 1
            if (num == 2):
                self.pop(node)
                num = 0
            node = node.next


if __name__ == '__main__':
    tmpList = list(map(int, input().split()))
    count = tmpList[0]
    n = tmpList[1]


    linkedList = CircleLinkedList(count)

    linkedList.repeatDelete(n)
    print(linkedList.ans)
