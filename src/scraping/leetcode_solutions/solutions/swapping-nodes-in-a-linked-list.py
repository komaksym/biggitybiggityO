# Time:  O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


class Solution(object):
    def swapNodes(self, head, k):
        left, right, curr = None, None, head
        while curr:
            k -= 1
            if right:
                right = right.__next__
            if k == 0:
                left = curr
                right = head
            curr = curr.__next__
        left.val, right.val = right.val, left.val
        return head
