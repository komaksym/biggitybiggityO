# Time:  O(n)

# z-function
class Solution(object):
    def sumScores(self, s):
        
       
        def z_function(s): 
            l, r = 0, 0
            for i in range(1, len(z)):
                if i <= r:
                    z[i] = min(r-i+1, z[i-l])
                while i+z[i] < len(z) and s[z[i]] == s[i+z[i]]:
                    z[i] += 1
                if i+z[i]-1 > r:
                    l, r = i, i+z[i]-1
            return z

        z = z_function(s)
        z[0] = len(s)
        return sum(z)
