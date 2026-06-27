class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=defaultdict(int)
        ans=[]
        l=len(nums)
        for i in range(len(nums)):
            n[nums[i]]+=1
        for key,value in n.items():
            if value>l//3:
                ans.append(key)
        return ans
        