class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        stack=[]
        stack.append(0)

        for i in range(1,2*n):
            curr=nums[i%n]
            while stack and nums[stack[-1]]<curr:
                res[stack.pop()]=curr
            if i<n:
                stack.append(i)
            if not stack:
                break
        return res


     
        