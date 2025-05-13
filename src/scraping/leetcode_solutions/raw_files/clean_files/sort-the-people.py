# Time:  O(nlogn)

# sort
class Solution(object):
    def sortPeople(self, names, heights):
        order = list(range(len(names)))
        order.sort(key=lambda x: heights[x], reverse=True)
        return [names[i] for i in order]
