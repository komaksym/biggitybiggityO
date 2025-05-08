# Time:  O(n)

class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


# linked list
class Solution(object):
    def mergeNodes(self, head):
        curr, zero = head.__next__, head
        while curr:
            if curr.val:
                zero.val += curr.val
            else:
                zero.next = curr if curr.__next__ else None
                zero = curr
            curr = curr.__next__
        return head
