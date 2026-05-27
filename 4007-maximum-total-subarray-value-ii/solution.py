from heapq import heappush, heappop

class Solution:
    class SegmentTree:
        def __init__(self, n):
            self.n = n
            self.maxValues = [0] * (4 * n)
            self.minValues = [0] * (4 * n)

        def insert(self, idx, val):
            self._insert(1, 0, self.n - 1, idx, val)

        def _insert(self, node, lo, hi, idx, val):
            if lo == hi:
                self.maxValues[node] = val
                self.minValues[node] = val
                return

            mid = (lo + hi) // 2

            if idx <= mid:
                self._insert(2 * node, lo, mid, idx, val)
            else:
                self._insert(2 * node + 1, mid + 1, hi, idx, val)

            self.maxValues[node] = max(
                self.maxValues[2 * node],
                self.maxValues[2 * node + 1]
            )
            self.minValues[node] = min(
                self.minValues[2 * node],
                self.minValues[2 * node + 1]
            )

        def query(self, l, r):
            return self._query(1, 0, self.n - 1, l, r)

        def _query(self, node, lo, hi, l, r):
            if r < lo or l > hi:
                return (float('inf'), float('-inf'))

            if l <= lo and hi <= r:
                return (
                    self.minValues[node],
                    self.maxValues[node]
                )

            mid = (lo + hi) // 2

            left = self._query(2 * node, lo, mid, l, r)
            right = self._query(2 * node + 1, mid + 1, hi, l, r)

            return (
                min(left[0], right[0]),
                max(left[1], right[1])
            )

    def maxTotalValue(self, nums, k):
        n = len(nums)

        st = self.SegmentTree(n)

        for i, num in enumerate(nums):
            st.insert(i, num)

        pq = []

        mn, mx = st.query(0, n - 1)
        heappush(pq, (-(mx - mn), 0, n - 1))

        visited = {(0, n - 1)}
        ans = 0

        while k > 0 and pq:
            neg_val, l, r = heappop(pq)
            val = -neg_val

            ans += val
            k -= 1

            if l + 1 <= r and (l + 1, r) not in visited:
                mn, mx = st.query(l + 1, r)
                visited.add((l + 1, r))
                heappush(pq, (-(mx - mn), l + 1, r))

            if l <= r - 1 and (l, r - 1) not in visited:
                mn, mx = st.query(l, r - 1)
                visited.add((l, r - 1))
                heappush(pq, (-(mx - mn), l, r - 1))

        return ans