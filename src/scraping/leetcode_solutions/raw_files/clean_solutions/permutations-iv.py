# Time:  O(n^2)

# combinatorics
class Solution(object):
    def permute(self, n, k):
        result = []
        cnt = [1]*n
        for i in range(len(cnt)-1):
            cnt[i+1] = min(cnt[i]*((i+2)//2), k)
        lookup = [False]*n
        for i in range(n):
            for j in range(n):
                if not (not lookup[j] and ((i == 0 and n%2 == 0) or (j+1)%2 == (1 if not result else (result[-1]%2)^1))):
                    continue
                if k <= cnt[n-1-i]:
                    break
                k -= cnt[n-1-i]
            else:
                return []
            lookup[j] = True
            result.append(j+1)
        return result


# Time:  O(n^2)
# combinatorics
class Solution2(object):
    def permute(self, n, k):
        result = []
        fact = [1]*(((n-1)+1)//2+1)
        for i in range(len(fact)-1):
            fact[i+1] = fact[i]*(i+1)
        lookup = [False]*n
        for i in range(n):
            cnt = fact[(n-1-i)//2]*fact[((n-1-i)+1)//2]
            for j in range(n):
                if not (not lookup[j] and ((i == 0 and n%2 == 0) or (j+1)%2 == (1 if not result else (result[-1]%2)^1))):
                    continue
                if k <= cnt:
                    break
                k -= cnt
            else:
                return []
            lookup[j] = True
            result.append(j+1)
        return result
