# Time:  O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, self.__next__)

class Solution(object):
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current.__next__ and current.next.__next__:
            next_one, next_two, next_three = current.__next__, current.next.__next__, current.next.next.__next__
            current.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            current = next_one
        return dummy.__next__

