# Time:  O(nlogn + mlogm)

# sort, two pointers
class Solution(object):
    def maximumCoins(self, heroes, monsters, coins):
        
        idxs1 = list(range(len(heroes)))
        idxs1.sort(key=lambda x: heroes[x])
        idxs2 = list(range(len(monsters)))
        idxs2.sort(key=lambda x: monsters[x])
        result = [0]*len(idxs1)
        i = curr = 0
        for idx in idxs1:
            for i in range(i, len(idxs2)):
                if monsters[idxs2[i]] > heroes[idx]:
                    break
                curr += coins[idxs2[i]]
            else:
                i = len(idxs2)
            result[idx] = curr
        return result
