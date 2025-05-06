# Time:  O(n)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseEvenLengthGroups(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, l = head, 2
        while prev.__next__:
            curr, cnt = prev, 0
            for _ in range(l):
                if not curr.__next__:
                    break
                cnt += 1
                curr = curr.__next__
            l += 1
            if cnt%2:
                prev = curr
                continue
            curr, last = prev.__next__, None
            for _ in range(cnt):
                curr.next, curr, last = last, curr.next, curr
            prev.next.next, prev.next, prev = curr, last, prev.next
        return head
