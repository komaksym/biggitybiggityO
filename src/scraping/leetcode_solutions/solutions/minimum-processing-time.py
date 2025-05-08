# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        K = 4
        processorTime.sort()
        tasks.sort(reverse=True)
        result = 0
        for i in range(len(processorTime)):
            for j in range(K):
                result = max(result, processorTime[i]+tasks[i*K+j])
        return result
