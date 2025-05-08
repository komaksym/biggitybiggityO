# Time:  O(n)

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        
        result = [0]*(n+1)
        for i, j, k in bookings:
            result[i-1] += k
            result[j] -= k
        for i in range(1, len(result)):
            result[i] += result[i-1]
        result.pop()
        return result
