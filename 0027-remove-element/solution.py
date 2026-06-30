class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=[]
        
        for i in range(len(nums)):
            if nums[i]!=val:
                a.append(nums[i])
        for i in range(len(a)):
            nums[i]=a[i]

        return len(a)
            
        