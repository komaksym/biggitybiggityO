# Time:  O(1)

# math
class Solution(object):
    def fillCups(self, amount):
        
        return max(max(amount), (sum(amount)+1)//2)


# Time:  O(1)
# constructive algorithms
class Solution2(object):
    def fillCups(self, amount):
        
        mx, total = max(amount), sum(amount)
        return mx if sum(amount)-mx <= mx else (total+1)//2
