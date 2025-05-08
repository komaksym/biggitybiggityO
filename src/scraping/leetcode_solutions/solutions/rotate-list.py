# Time:  O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.__next__))

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.__next__:
            return head

        n, cur = 1, head
        while cur.__next__:
            cur = cur.__next__
            n += 1
        cur.next = head

        cur, tail = head, cur
        for _ in range(n - k % n):
            tail = cur
            cur = cur.__next__
        tail.next = None

        return cur


