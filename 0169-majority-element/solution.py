class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=defaultdict(int)
        for i in range(len(nums)):
            a[nums[i]]+=1
        for key,value in a.items():
                if value>len(nums)/2:
                        return key
        return 0
                

        