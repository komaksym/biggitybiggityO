# Time:  O(nlogn + mlogm)

# greedy, sort
class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        result = 0
        for x in trainers:
            if players[result] > x:
                continue
            result += 1
            if result == len(players):
                break
        return result
