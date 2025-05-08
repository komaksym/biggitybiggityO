# Time:  O(logn)

class Solution(object):
    def confusingNumberII(self, n):
        """
        :type n: int
        :rtype: int
        """
        lookup = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        centers = {"0":"0", "1":"1", "8":"8"}
        def totalCount(n): 
            s = str(n)
            total = 0 
            p = len(lookup)**(len(s)-1)
            for i in range(len(s)+1):
                if i == len(s):
                    total += 1
                    break
                smaller = sum(int(c < s[i]) for c in lookup.keys())
                total += smaller * p
                if s[i] not in lookup:
                    break
                p //= len(lookup)
            return total-1 

        def validCountInLessLength(n): 
            s = str(n)
            valid = 0
            total = len(centers)
            for i in range(1, len(s), 2): 
                if i == 1:
                    valid += len({c for c in centers.keys() if c != '0'})
                else:
                    valid += total * (len(lookup)-1)
                    total *= len(lookup)
            total = 1
            for i in range(2, len(s), 2): 
                valid += total * (len(lookup)-1)
                total *= len(lookup)
            return valid

        def validCountInFullLength(n): 
            s = str(n)
            half_s = s[:(len(s)+1)//2]
            total = 0
            choices = centers if (len(s) % 2) else lookup
            p = int(len(lookup)**(len(half_s)-2) * len(choices))
            for i in range(len(half_s)):
                if i == len(half_s)-1:
                    total += sum(int(c < half_s[i]) for c in choices.keys() if i != 0 or c != '0')
                    if half_s[i] not in choices:
                        break
                    tmp = list(half_s)+[lookup[half_s[i]] for i in reversed(range(len(half_s)-(len(s) % 2)))]
                    total += 0 < int("".join(tmp)) <= n
                    break
                smaller = sum(int(c < half_s[i]) for c in lookup.keys() if i != 0 or c != '0')
                total += smaller * p
                if half_s[i] not in lookup:
                    break
                p //= len(lookup)
            return total

        return totalCount(n) - validCountInLessLength(n) - validCountInFullLength(n)


# Time:  O(logn)
class Solution2(object):
    def confusingNumberII(self, n):
        """
        :type n: int
        :rtype: int
        """
        lookup = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        centers = {"0":"0", "1":"1", "8":"8"}
        def totalCount(n): 
            s = str(n)
            total = 0 
            p = len(lookup)**(len(s)-1)
            for i in range(len(s)+1):
                if i == len(s):
                    total += 1
                    break
                smaller = sum(int(c < s[i]) for c in lookup.keys())
                total += smaller * p
                if s[i] not in lookup:
                    break
                p //= len(lookup)
            return total

        def validCountInLessLength(n): 
            s = str(n)
            valid = 0
            total = len(centers)
            for i in range(1, len(s), 2): 
                if i == 1:
                    valid += len(centers)
                else:
                    valid += total * (len(lookup)-1)
                    total *= len(lookup)
            total = 1
            for i in range(2, len(s), 2): 
                valid += total * (len(lookup)-1)
                total *= len(lookup)
            return valid

        def validCountInFullLength(n): 
            s = str(n)
            half_s = s[:(len(s)+1)//2]
            total = 0
            choices = centers if (len(s) % 2) else lookup
            p = int(len(lookup)**(len(half_s)-2) * len(choices))
            for i in range(len(half_s)):
                if i == len(half_s)-1:
                    total += sum(int(c < half_s[i]) for c in choices.keys() if len(s) != 2 or c != '0')
                    if half_s[i] not in choices:
                        break
                    tmp = list(half_s)+[lookup[half_s[i]] for i in reversed(range(len(half_s)-(len(s) % 2)))]
                    total += int("".join(tmp)) <= n
                    break
                smaller = sum(int(c < half_s[i]) for c in lookup.keys() if i != 0 or c != '0')
                total += smaller * p
                if half_s[i] not in lookup:
                    break
                p //= len(lookup)
            return total

        def f(n): 
            return totalCount(n) - validCountInLessLength(n) - validCountInFullLength(n)

        return f(n) - f(0) 
