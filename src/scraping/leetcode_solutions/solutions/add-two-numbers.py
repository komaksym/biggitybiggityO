# Time:  O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)
        current, carry = dummy, 0

        while l1 or l2:
            val = carry
            if l1:
                val += l1.val
                l1 = l1.__next__
            if l2:
                val += l2.val
                l2 = l2.__next__
            carry, val = divmod(val, 10)
            current.next = ListNode(val)
            current = current.__next__

        if carry == 1:
            current.next = ListNode(1)

        return dummy.__next__

