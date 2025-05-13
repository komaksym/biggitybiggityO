# Time:  O(v * n)

class Solution(object):
    def pourWater(self, heights, V, K):
        for _ in range(V):
            best = K
            for d in (-1, 1):
                i = K
                while 0 <= i+d < len(heights) and \
                      heights[i+d] <= heights[i]:
                    if heights[i+d] < heights[i]: best = i+d
                    i += d
                if best != K:
                    break
            heights[best] += 1
        return heights

