# Time:  O(n)
# Space: O(1)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        def reverseList(head):
            dummy = ListNode()
            while head:
                dummy.next, head.next, head = head, dummy.next, head.next
            return dummy.__next__

        dummy = ListNode(next=head)
        slow = fast = dummy
        while fast.__next__ and fast.next.__next__:
            slow, fast = slow.__next__, fast.next.__next__
        result = 0
        head2 = reverseList(slow)
        while head:
            result = max(result, head.val+head2.val)
            head, head2 = head.__next__, head2.__next__
        return result
