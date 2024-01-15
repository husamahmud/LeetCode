class Solution(object):
    def findWinners(self, matches):
        players = set()
        for match in matches:
            players.add(match[0])
            players.add(match[1])

        winners = set()
        for match in matches:
            winners.add(match[1])

        losers = {}
        for match in matches:
            player = match[1]
            if player in losers:
                losers[player] += 1
            else:
                losers[player] = 1

        ans2 = []
        for key, val in losers.items():
            if val == 1:
                ans2.append(key)

        ans1 = players - winners
        return sorted(ans1), sorted(ans2)
