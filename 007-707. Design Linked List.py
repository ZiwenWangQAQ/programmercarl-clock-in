class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index):
        if index >= self.length:
            return -1

        ans = self.head
        while index:
            ans = ans.next
            index -= 1

        return ans.val

    def addAtHead(self, val):
        new_head = Node(val)

        if not self.head:
            self.head = new_head
        else:
            new_head.next = self.head
            self.head = new_head

        self.length += 1

    def addAtTail(self, val):
        new_tail = Node(val)

        if not self.head:
            self.head = new_tail
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_tail

        self.length += 1

    def addAtIndex(self, index, val):
        if index > self.length:
            return

        new_node = Node(val)

        if index == 0:
            if not self.head:
                self.head = new_node
                self.length += 1
                return
            new_node.next = self.head
            self.head = new_node

        elif index == self.length:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = new_node

        else:
            node = self.head
            while index - 1:
                node = node.next
                index -= 1

            new_node.next = node.next
            node.next = new_node

        self.length += 1

    def deleteAtIndex(self, index):
        if index == 0 and self.length == 0:
            return

        if index > self.length - 1:
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            node = self.head
            while index - 1:
                node = node.next
                index -= 1

            node.next = node.next.next
            self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
