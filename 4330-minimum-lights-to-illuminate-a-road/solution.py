class Solution:
    def minLights(self, lights: list[int]) -> int:
        n = len(lights)

        diff = [0] * (n + 2)

        # Step 1: mark coverage of existing bulbs
        for i, v in enumerate(lights):
            if v > 0:
                l = max(0, i - v)
                r = min(n - 1, i + v)

                diff[l] += 1
                diff[r + 1] -= 1

        # Step 2: build visibility array
        visible = [False] * n
        cur = 0

        for i in range(n):
            cur += diff[i]
            visible[i] = cur > 0

        # Step 3: greedy for new bulbs
        ans = 0
        i = 0

        while i < n:
            if visible[i]:
                i += 1
            else:
                ans += 1
                i += 3   # one bulb covers i, i+1, i+2

        return ans