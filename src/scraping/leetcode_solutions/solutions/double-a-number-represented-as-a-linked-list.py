# Time:  O(n)

# linked list
class Solution(object):
    def doubleIt(self, head):
        if head.val >= 5:
            head = ListNode(0, head)
        curr = head
        while curr:
            curr.val = (curr.val*2)%10
            if curr.__next__ and curr.next.val >= 5:
                curr.val += 1
            curr = curr.__next__
        return head
