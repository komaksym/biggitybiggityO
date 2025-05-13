# Time:  O(1)

# freq table
class Solution(object):
    def bestHand(self, ranks, suits):
        LOOKUP = ["", "High Card", "Pair", "Three of a Kind", "Three of a Kind", "Three of a Kind"]
        if all(suits[i] == suits[0] for i in range(1, len(suits))):
            return "Flush"
        cnt = [0]*13
        for x in ranks:
            cnt[x-1] += 1
        return LOOKUP[max(cnt)]
