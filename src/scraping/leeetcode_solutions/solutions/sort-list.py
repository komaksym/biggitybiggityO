# Time:  O(nlogn)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.__next__))

class Solution(object):
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        if head == None or head.__next__ == None:
            return head

        fast, slow, prev = head, head, None
        while fast != None and fast.__next__ != None:
            prev, fast, slow = slow, fast.next.__next__, slow.__next__
        prev.next = None

        sorted_l1 = self.sortList(head)
        sorted_l2 = self.sortList(slow)

        return self.mergeTwoLists(sorted_l1, sorted_l2)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)

        cur = dummy
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.__next__
            else:
                cur.next, cur, l2 = l2, l2, l2.__next__

        if l1 != None:
            cur.next = l1
        if l2 != None:
            cur.next = l2

        return dummy.__next__

