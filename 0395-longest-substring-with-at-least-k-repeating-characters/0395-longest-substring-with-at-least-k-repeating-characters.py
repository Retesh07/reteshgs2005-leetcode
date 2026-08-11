from collections import defaultdict

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0

        for l in range(len(s)):
            hashmap = defaultdict(int)

            for r in range(l, len(s)):
                hashmap[s[r]] += 1

                valid = True

                for h in hashmap.values():
                    if h < k:
                        valid = False
                        break

                if valid:
                    res = max(res, r - l + 1)

        return res