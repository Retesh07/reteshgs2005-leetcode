class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        m1 = defaultdict(int)
        m2 = defaultdict(int)

        for ch in s1:
            m1[ch] += 1

        l = 0
        for r in range(len(s2)):
            m2[s2[r]] += 1

            if r - l + 1 > len(s1):
                m2[s2[l]] -= 1
                if m2[s2[l]] == 0:
                    del m2[s2[l]]
                l += 1

            if m1 == m2:
                return True

        return False