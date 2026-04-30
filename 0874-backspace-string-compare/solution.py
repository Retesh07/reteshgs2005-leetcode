class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def next_valid(st, i):
            skip = 0

            while i >= 0:
                if st[i] == "#":
                    skip += 1

                elif skip > 0:
                    skip -= 1

                else:
                    return i   # valid character found

                i -= 1

            return -1

        i = len(s) - 1
        j = len(t) - 1

        while i >= 0 or j >= 0:

            i = next_valid(s, i)
            j = next_valid(t, j)

            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False

            elif i != j:     # one string finished earlier
                return False

            i -= 1
            j -= 1

        return True