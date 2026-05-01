class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.pre = [0] * (n + 1)

        for i in range(n):
            self.pre[i + 1] = self.pre[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.pre[right + 1] - self.pre[left]