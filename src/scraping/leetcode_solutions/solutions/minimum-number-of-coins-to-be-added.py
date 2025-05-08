# Time:  O(nlogn + logt)

# lc0330
# sort, greedy
class Solution(object):
    def minimumAddedCoins(self, coins, target):
        
        coins.sort()
        result = reachable = 0
        for x in coins:
           
           
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
            reachable += x
        while not reachable >= target:
            result += 1
            reachable += reachable+1
        return result


# Time:  O(nlogn + logt)
# lc0330
# sort, greedy
class Solution2(object):
    def minimumAddedCoins(self, coins, target):
        
        coins.sort()
        result = reachable = 0
        for x in coins:
            while not reachable >= x-1:
                result += 1
                reachable += reachable+1
                if reachable >= target:
                    return result
            reachable += x
            if reachable >= target:
                return result
        while not reachable >= target:
            result += 1
            reachable += reachable+1
        return result
