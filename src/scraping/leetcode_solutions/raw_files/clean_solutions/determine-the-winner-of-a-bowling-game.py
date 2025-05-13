# Time:  O(n)

# array
class Solution(object):
    def isWinner(self, player1, player2):
        k = 2
        def f(arr):
            result = cnt = 0
            for i in range(len(arr)):
                result += 2*arr[i] if cnt else arr[i]
                cnt += (arr[i] == 10)
                if i-k >= 0:
                    cnt -= (arr[i-k] == 10)
            return result

        a, b = f(player1), f(player2)
        return 1 if a > b else 2 if a < b else 0
