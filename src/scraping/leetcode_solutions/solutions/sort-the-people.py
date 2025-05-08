# Time:  O(nlogn)

# sort
class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        order = list(range(len(names)))
        order.sort(key=lambda x: heights[x], reverse=True)
        return [names[i] for i in order]
