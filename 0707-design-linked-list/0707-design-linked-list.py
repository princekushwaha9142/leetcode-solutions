class Node(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        self.dummy = Node(0)
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy.next
        for _ in range(index):
            cur = cur.next
        return cur.val
    def addAtHead(self, val):
        self.addAtIndex(0, val)
    def addAtTail(self, val):
        self.addAtIndex(self.size, val)
    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = Node(val, prev.next)
        self.size += 1
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        prev = self.dummy
        for _ in range(index):
            prev = prev.next
        prev.next = prev.next.next
        self.size -= 1