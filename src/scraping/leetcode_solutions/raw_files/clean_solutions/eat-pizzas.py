# Time:  O(nlogn)

# sort, greedy
class Solution(object):
    def maxWeight(self, pizzas):
        l = len(pizzas)//4
        pizzas.sort(reverse=True)
        return sum(pizzas[i] for i in range((l+1)//2))+sum(pizzas[i] for i in range((l+1)//2+1, ((l+1)//2+1)+(l//2)*2, 2))
