class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Remove consecutive *
        new_p = []
        for c in p:
            if not new_p or c != "*" or new_p[-1] != "*":
                new_p.append(c)
        p = "".join(new_p)

        dp = {}

        def lcs(i, j):
            if j == len(p):
                return i == len(s)

            if (i, j) in dp:
                return dp[(i, j)]

            if p[j] == "*":
                dp[(i, j)] = (
                    lcs(i, j + 1)
                    or (i < len(s) and lcs(i + 1, j))
                )
                return dp[(i, j)]

            if i < len(s) and (p[j] == "?" or s[i] == p[j]):
                dp[(i, j)] = lcs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return False

        return lcs(0, 0)