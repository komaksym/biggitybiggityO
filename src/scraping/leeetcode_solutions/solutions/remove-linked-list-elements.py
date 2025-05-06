# Time:  O(n)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev, curr = dummy, dummy.__next__

        while curr:
            if curr.val == val:
                prev.next = curr.__next__
            else:
                prev = curr

            curr = curr.__next__

        return dummy.__next__



