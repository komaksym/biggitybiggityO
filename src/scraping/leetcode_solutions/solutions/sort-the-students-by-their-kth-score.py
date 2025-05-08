# Time:  O(mlogm)

# sort
class Solution(object):
    def sortTheStudents(self, score, k):
        
        score.sort(key=lambda x: x[k], reverse=True)
        return score
