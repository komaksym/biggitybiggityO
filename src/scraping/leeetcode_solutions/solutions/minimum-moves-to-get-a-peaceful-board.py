# Time:  O(n)

# counting sort, greedy
class Solution(object):
    def minMoves(self, rooks):
        
        def count(arr):
            cnt = [0]*len(arr)
            for x in arr:
                cnt[x] += 1
            return sum(abs(i-x) for i, x in enumerate(x for x, cnt in enumerate(cnt) for _ in range(cnt)))

        return sum(count(arr) for arr in zip(*rooks))


# Time:  O(n)
# prefix sum, greedy
class Solution2(object):
    def minMoves(self, rooks):
        
        def count(arr):
            cnt = [0]*len(arr)
            for x in arr:
                cnt[x] += 1
            result = bal = 0
            for i in range(len(rooks)):
                bal += cnt[i]-1
                result += abs(bal)
            return result

        return sum(count(arr) for arr in zip(*rooks))
    
