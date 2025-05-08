# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        head = dummy = ListNode(next=head)
        while head:
            for _ in range(m):
                if not head.__next__:
                    return dummy.__next__
                head = head.__next__
            prev = head
            for _ in range(n):
                if not head.__next__:
                    prev.next = None
                    return dummy.__next__
                head = head.__next__
            prev.next = head.__next__
        return dummy.__next__
