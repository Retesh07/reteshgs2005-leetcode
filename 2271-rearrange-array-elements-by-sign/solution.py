class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        posind=0
        negin=1
        ans = [0] * len(nums)
        for num in nums:
            if num>0:
                ans[posind]=num
                posind+=2
            else:
                ans[negin]=num
                negin+=2

        return ans