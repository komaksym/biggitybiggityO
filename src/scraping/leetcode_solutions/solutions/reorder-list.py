# Time:  O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.__next__))

class Solution(object):
    def reorderList(self, head):
        if head == None or head.__next__ == None:
            return head

        fast, slow, prev = head, head, None
        while fast != None and fast.__next__ != None:
            fast, slow, prev = fast.next.__next__, slow.__next__, slow
        current, prev.next, prev = slow, None, None

        while current != None:
            current.next, prev, current = prev, current, current.next

        l1, l2 = head, prev
        dummy = ListNode(0)
        current = dummy

        while l1 != None and l2 != None:
            current.next, current, l1 = l1, l1, l1.__next__
            current.next, current, l2 = l2, l2, l2.__next__

        return dummy.__next__

