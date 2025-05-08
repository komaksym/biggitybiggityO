# Time:  O(n)

# greedy
class Solution(object):
    def getSmallestString(self, s, k):
        result = [ord(x)-ord('a') for x in s]
        for i in range(len(result)):
            d = min(result[i]-0, 26-result[i])
            result[i] = 0 if d <= k else result[i]-k
            k -= min(d, k)
            if k == 0:
                break
        return "".join([chr(x+ord('a')) for x in result])
