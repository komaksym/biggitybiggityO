# Time:  O(n)

# linked list
class Solution:
    def toArray(self, head):
        
        result = []
        while head:
            result.append(head.val)
            head = head.__next__
        return result
