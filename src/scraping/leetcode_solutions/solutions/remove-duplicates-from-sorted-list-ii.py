# Time:  O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.__next__))

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        pre, cur = dummy, head
        while cur:
            if cur.__next__ and cur.next.val == cur.val:
                val = cur.val
                while cur and cur.val == val:
                    cur = cur.__next__
                pre.next = cur
            else:
                pre.next = cur
                pre = cur
                cur = cur.__next__
        return dummy.__next__

