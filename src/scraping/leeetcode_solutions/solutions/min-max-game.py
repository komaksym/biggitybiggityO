# Time:  O(n)

# simulation, optimized from solution2
class Solution(object):
    def minMaxGame(self, nums):
        
        n = len(nums)
        while n != 1:
            new_q = []
            for i in range(n//2):
                nums[i] = min(nums[2*i], nums[2*i+1]) if i%2 == 0 else max(nums[2*i], nums[2*i+1])
            n //= 2
        return nums[0]


# Time:  O(n)
# simulation
class Solution2(object):
    def minMaxGame(self, nums):
        
        q = nums[:]
        while len(q) != 1:
            new_q = []
            for i in range(len(q)//2):
                new_q.append(min(q[2*i], q[2*i+1]) if i%2 == 0 else max(q[2*i], q[2*i+1]))
            q = new_q
        return q[0]
