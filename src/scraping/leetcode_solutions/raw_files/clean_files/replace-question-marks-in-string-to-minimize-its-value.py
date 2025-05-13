# Time:  O(n + 26 * log(26))

# greedy, counting sort, prefix sum
class Solution(object):
    def minimizeStringValue(self, s):
        def counting_sort(cnt):
            for i in range(len(cnt)):
                for _ in range(cnt[i]):
                    yield i
        
        def fill(cnt):
            result = [0]*26
            a = [(x, i) for i, x in enumerate(cnt)]
            a.sort()
            total = s.count('?')
            curr = 0
            for i in range(len(a)-1):
                if curr+(a[i+1][0]-a[i][0])*(i+1) > total:
                    break
                curr += (a[i+1][0]-a[i][0])*(i+1)
            else:
                i = len(a)-1
            q, r = divmod(total-curr, i+1)
            for j in range(i+1):
                result[a[j][1]] = (a[i][0]-a[j][0])+q
            cnt2 = [0]*26
            for j in range(i+1):
                cnt2[a[j][1]] += 1
            it = counting_sort(cnt2)
            for _ in range(r):
                result[next(it)] += 1
            return result
    
        cnt = [0]*26
        for x in s:
            if x == '?':
                continue
            cnt[ord(x)-ord('a')] += 1
        it = counting_sort(fill(cnt))
        result = list(s)
        for i in range(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)


# Time:  O(n + n * log(26))
import heapq


# greedy, counting sort, heap
class Solution2(object):
    def minimizeStringValue(self, s):
        def counting_sort(cnt):
            for i in range(len(cnt)):
                for _ in range(cnt[i]):
                    yield i

        cnt = [0]*26
        for x in s:
            if x == '?':
                continue
            cnt[ord(x)-ord('a')] += 1
        min_heap = [(x, i) for i, x in enumerate(cnt)]
        heapq.heapify(min_heap)
        cnt2 = [0]*26
        for _ in range(s.count('?')):
            c, i = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (c+1, i))
            cnt2[i] += 1
        it = counting_sort(cnt2)
        result = list(s)
        for i in range(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)


# Time:  O(n + n * 26)
# greedy, counting sort
class Solution3(object):
    def minimizeStringValue(self, s):
        def counting_sort(cnt):
            for i in range(len(cnt)):
                for _ in range(cnt[i]):
                    yield i
    
        cnt = [0]*26
        for x in s:
            if x == '?':
                continue
            cnt[ord(x)-ord('a')] += 1
        cnt2 = [0]*26
        for _ in range(s.count('?')):
            i = min(range(len(cnt)), key=lambda x: cnt[x]+cnt2[x])
            cnt2[i] += 1
        it = counting_sort(cnt2)
        result = list(s)
        for i in range(len(result)):
            if result[i] != '?':
                continue
            result[i] = chr(ord('a')+next(it))
        return "".join(result)
