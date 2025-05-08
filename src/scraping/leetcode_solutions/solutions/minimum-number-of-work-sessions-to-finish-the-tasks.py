# Time:  O(n * 2^n)

class Solution(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        dp = [float("inf") for _ in range(1<<len(tasks))]
        dp[0] = 0
        for mask in range(len(dp)-1):
            basis = 1
            for task in tasks:
                new_mask = mask|basis
                basis <<= 1
                if new_mask == mask:
                    continue
                if dp[mask]%sessionTime + task > sessionTime:
                    task += sessionTime-dp[mask]%sessionTime 
                dp[new_mask] = min(dp[new_mask], dp[mask]+task)
        return (dp[-1]+sessionTime-1)//sessionTime


# Time:  O(n * 2^n)
class Solution2(object):
    def minSessions(self, tasks, sessionTime):
        """
        :type tasks: List[int]
        :type sessionTime: int
        :rtype: int
        """
        dp = [[float("inf")]*2 for _ in range(1<<len(tasks))]
        dp[0] = [0, sessionTime]
        for mask in range(len(dp)-1):
            basis = 1
            for task in tasks:
                new_mask = mask|basis
                basis <<= 1
                if new_mask == mask:
                    continue
                if dp[mask][1]+task <= sessionTime:
                    dp[new_mask] = min(dp[new_mask], [dp[mask][0], dp[mask][1]+task])
                else:
                    dp[new_mask] = min(dp[new_mask], [dp[mask][0]+1, task])
        return dp[-1][0]
