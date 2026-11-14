class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        sums = float('inf')

        for k in range(l, r + 1):
            i = 0
            j = k
            trial = sum(nums[:k])

            while True:
                if trial > 0:
                    sums = min(sums, trial)

                if j == len(nums):
                    break

                trial += nums[j]
                trial -= nums[i]

                i += 1
                j += 1

        return sums if sums != float('inf') else -1