# Time:  O(n)

class ListNode(object):
    def __init__(self, val=0, next=None):
        pass


# mono stack
class Solution(object):
    def removeNodes(self, head):
        stk = []
        while head:
            while stk and stk[-1].val < head.val:
                stk.pop()
            if stk:
                stk[-1].next = head
            stk.append(head)
            head = head.__next__
        return stk[0]
