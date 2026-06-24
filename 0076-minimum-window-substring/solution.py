class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash = defaultdict(int)

        if len(t) > len(s):
            return ""

        for j in range(len(t)):
            hash[t[j]] += 1

        m = len(t)
        l = 0
        minlen = float('inf')
        cnt = 0
        st = -1

        for r in range(len(s)):
            if s[r] in hash:
                hash[s[r]] -= 1
                if hash[s[r]] >= 0:
                    cnt += 1

            while cnt == m:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    st = l

                if s[l] in hash:
                    hash[s[l]] += 1
                    if hash[s[l]] > 0:
                        cnt -= 1
                l += 1

        return "" if minlen == float('inf') else s[st:st + minlen]