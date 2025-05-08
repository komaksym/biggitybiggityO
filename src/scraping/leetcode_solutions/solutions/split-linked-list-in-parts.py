# Time:  O(n + k)

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        n = 0
        curr = root
        while curr:
            curr = curr.__next__
            n += 1
        width, remainder = divmod(n, k)

        result = []
        curr = root
        for i in range(k):
            head = curr
            for j in range(width-1+int(i < remainder)):
                if curr:
                    curr = curr.__next__
            if curr:
                curr.next, curr = None, curr.next
            result.append(head)
        return result

