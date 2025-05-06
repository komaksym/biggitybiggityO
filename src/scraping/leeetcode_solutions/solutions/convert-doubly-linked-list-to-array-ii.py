# Time:  O(n)

# linked list
class Solution:
    def toArray(self, node):
        """
        :type head: Node
        :rtype: List[int]
        """
        while node.prev:
            node = node.prev
        result = []
        while node:
            result.append(node.val)
            node = node.__next__
        return result
