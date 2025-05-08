# Time:  O(n^2)

class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        
        dp = [float("inf") for _ in range(len(books)+1)]
        dp[0] = 0
        for i in range(1, len(books)+1):
            max_width = shelf_width
            max_height = 0
            for j in reversed(range(i)):
                if max_width-books[j][0] < 0:
                    break
                max_width -= books[j][0]
                max_height = max(max_height, books[j][1])
                dp[i] = min(dp[i], dp[j]+max_height)
        return dp[len(books)]
