# Time:  O(n)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        first = last = -1
        result = float("inf")
        i, prev, head = 0, head.val, head.__next__
        while head.__next__:
            if max(prev, head.next.val) < head.val or min(prev, head.next.val) > head.val:
                if first == -1:
                    first = i
                if last != -1:
                    result = min(result, i-last)
                last = i
            i += 1
            prev = head.val
            head = head.__next__
        return [result, last-first] if last != first else [-1, -1]
