# Time:  O(n)
# Space: O(m)

# hash table, linked list
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        lookup = set(nums)
        curr = dummy = ListNode(0, head)
        while curr.__next__:
            if curr.next.val not in lookup:
                curr = curr.__next__
            else:
                curr.next = curr.next.__next__
        return dummy.__next__
