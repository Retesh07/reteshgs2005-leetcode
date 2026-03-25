class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp = {}
        used = set()

        for i in range(len(s)):
            if s[i] in mp:
                if mp[s[i]] != t[i]:
                    return False
            else:
                if t[i] in used:
                    return False
                mp[s[i]] = t[i]
                used.add(t[i])

        return True