

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        dq = deque()
        ans = 0
        cost = 0
        right = len(nums) - 1

        for left in range(len(nums) - 1, -1, -1):
            x = nums[left]

            while dq and nums[dq[0]] <= x:
                idx = dq.popleft()
                end = dq[0] if dq else right + 1
                cost += (x - nums[idx]) * (end - idx)

            dq.appendleft(left)

            while cost > k:
                cost -= nums[dq[-1]] - nums[right]

                if dq[-1] == right:
                    dq.pop()

                right -= 1

            ans += right - left + 1

        return ans
