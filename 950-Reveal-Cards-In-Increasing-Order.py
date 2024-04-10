class Solution(object):
    def deckRevealedIncreasing(self, deck):
        n = len(deck)
        res = [0] * n
        q = deque(range(n))
        deck.sort()        

        for card in deck:
            i = q.popleft()
            res[i] = card
            if q:
                q.append(q.popleft())

        return res