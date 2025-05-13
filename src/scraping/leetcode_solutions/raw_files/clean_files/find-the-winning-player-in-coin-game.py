# Time:  O(1)

# math
class Solution(object):
    def losingPlayer(self, x, y):
        return "Alice" if min(x, y//4)%2 else "Bob"
