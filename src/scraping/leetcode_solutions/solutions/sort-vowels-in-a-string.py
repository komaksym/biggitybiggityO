# Time:  O(n)

# counting sort
class Solution(object):
    def sortVowels(self, s):
        def inplace_counting_sort(nums, reverse=False):  # Time: O(n)
            if not nums:
                return
            count = [0]*(max(nums)+1)
            for num in nums:
                count[num] += 1
            for i in range(1, len(count)):
                count[i] += count[i-1]
            for i in reversed(range(len(nums))):  # inplace but unstable sort
                while nums[i] >= 0:
                    count[nums[i]] -= 1
                    j = count[nums[i]]
                    nums[i], nums[j] = nums[j], ~nums[i]
            for i in range(len(nums)):
                nums[i] = ~nums[i]  # restore values
            if reverse:  # unstable sort
                nums.reverse()
    
        VOWELS = "AEIOUaeiou"
        LOOKUP = {x:i for i, x in enumerate(VOWELS)}
        vowels = [LOOKUP[x] for x in s if x in LOOKUP]
        inplace_counting_sort(vowels, reverse=True)
        return "".join(VOWELS[vowels.pop()] if x in LOOKUP else x for x in s)


# Time:  O(nlogn)
# sort
class Solution2(object):
    def sortVowels(self, s):
        VOWELS = "AEIOUaeiou"
        LOOKUP = set(VOWELS)
        vowels = [x for x in s if x in LOOKUP]
        vowels.sort(reverse=True)
        return "".join(vowels.pop() if x in LOOKUP else x for x in s)
