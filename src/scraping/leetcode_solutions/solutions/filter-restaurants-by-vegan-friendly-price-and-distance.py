# Time:  O(rlogr), r is the number of result

class Solution(object):
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        
        result, lookup = [], {}
        for j, (i, _, v, p, d) in enumerate(restaurants):
            if v >= veganFriendly and p <= maxPrice and d <= maxDistance:
                lookup[i] = j
                result.append(i)
        result.sort(key=lambda i: (-restaurants[lookup[i]][1], -restaurants[lookup[i]][0]))
        return result
