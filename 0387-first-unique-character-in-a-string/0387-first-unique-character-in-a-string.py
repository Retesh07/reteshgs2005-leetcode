class Solution:
    def firstUniqChar(self, s: str) -> int:
        maps=defaultdict(list)
        k=float("inf")
        for i,ch in enumerate(s):
            maps[ch].append(i)
        for m in maps.values():
            if len(m)==1:
                k=min(m[0],k)
        return k if k!=float("inf") else -1
                