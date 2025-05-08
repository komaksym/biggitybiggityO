# Time:  O(n)

# linked list
class Solution(object):
    def frequenciesOfElements(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = dummy = ListNode(0)
        cnt = 0
        while head:
            cnt += 1
            if not head.__next__ or head.next.val != head.val:
                curr.next = ListNode(cnt)
                curr = curr.__next__
                cnt = 0
            head = head.__next__
        return dummy.__next__
