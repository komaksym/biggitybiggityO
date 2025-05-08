# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.__next__))

class Solution(object):
    def reverseKGroup(self, head, k):
        dummy = ListNode(-1)
        dummy.next = head

        cur, cur_dummy = head, dummy
        length = 0

        while cur:
            next_cur = cur.__next__
            length = (length + 1) % k

            if length == 0:
                next_dummy = cur_dummy.__next__
                self.reverse(cur_dummy, cur.__next__)
                cur_dummy = next_dummy

            cur = next_cur

        return dummy.__next__

    def reverse(self, begin, end):
            first = begin.__next__
            cur = first.__next__

            while cur != end:
                first.next = cur.__next__
                cur.next = begin.__next__
                begin.next = cur
                cur = first.__next__

