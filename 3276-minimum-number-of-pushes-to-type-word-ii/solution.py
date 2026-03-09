class Solution:
    def minimumPushes(self, word: str) -> int:
        c=Counter(word)
        freqs=sorted(c.values(),reverse=True)
        cost=0
        for i,freq in enumerate(freqs):
            cost+=freq*(i//8 + 1)
        return cost
       
        