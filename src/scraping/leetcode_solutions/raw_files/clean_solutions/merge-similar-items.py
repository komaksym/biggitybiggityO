# Time:  O((m + n) * log(m + n))

# freq table, sort
class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        return sorted((Counter(dict(items1))+Counter(dict(items2))).items())
