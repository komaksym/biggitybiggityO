# Time:  O(n)

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        
        rule = {"type":0, "color":1, "name":2}
        return sum(item[rule[ruleKey]] == ruleValue for item in items)
