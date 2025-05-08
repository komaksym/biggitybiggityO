# Time:  O(1)
# Space: O(1)

class Solution(object):
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        if node and node.__next__:
            node_to_delete = node.__next__
            node.val = node_to_delete.val
            node.next = node_to_delete.__next__
            del node_to_delete

