# Time:  O(n)

class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        curr = head
        while curr:
            if curr.child:
                curr_next = curr.__next__
                curr.child.prev = curr
                curr.next = curr.child
                last_child = curr
                while last_child.__next__:
                    last_child = last_child.__next__
                if curr_next:
                    last_child.next = curr_next
                    curr_next.prev = last_child
                curr.child = None
            curr = curr.__next__
        return head

