"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        if not head:
            return None
        curr = head
        while curr:
            if curr.child:
                next_node = curr.next
                child_head = curr.child

                child_tail = child_head
                while child_tail.next:
                    child_tail = child_tail.next
                child_tail.next = next_node
                if next_node:
                    next_node.prev = child_tail
                curr.next = child_head
                child_head.prev = curr
                curr.child = None
            curr = curr.next
        return head