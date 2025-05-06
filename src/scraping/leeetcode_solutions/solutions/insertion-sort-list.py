# Time:  O(n ^ 2)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.__next__))
        else:
            return "Nil"

class Solution(object):
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        if head is None or self.isSorted(head):
            return head

        dummy = ListNode(-2147483648)
        dummy.next = head
        cur, sorted_tail = head.__next__, head
        while cur:
            prev = dummy
            while prev.next.val < cur.val:
                prev = prev.__next__
            if prev == sorted_tail:
                cur, sorted_tail = cur.__next__, cur
            else:
                cur.next, prev.next, sorted_tail.next = prev.next, cur, cur.next
                cur = sorted_tail.__next__

        return dummy.__next__

    def isSorted(self, head):
        while head and head.__next__:
            if head.val > head.next.val:
                return False
            head = head.__next__
        return True

