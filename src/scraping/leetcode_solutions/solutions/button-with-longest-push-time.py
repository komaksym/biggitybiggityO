# Time:  O(n)

# array
class Solution(object):
    def buttonWithLongestTime(self, events):
        
        return -max((events[i][1]-(events[i-1][1] if i-1 >= 0 else 0), -events[i][0])for i in range(len(events)))[1]
