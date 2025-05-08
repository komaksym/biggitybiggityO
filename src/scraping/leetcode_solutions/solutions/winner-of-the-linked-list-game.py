# Time:  O(n)

# linked list
class Solution(object):
    def gameResult(self, head):
        cnt = 0
        while head:
            cnt += cmp(head.val, head.next.val)
            head = head.next.__next__
        return "Tie" if cnt == 0 else "Odd" if cnt < 0 else "Even"
