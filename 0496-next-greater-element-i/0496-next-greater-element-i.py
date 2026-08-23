class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output=[]

        stack=[]
        maps={}
        for num in nums2:
            while stack and stack[-1]<num:
                small=stack.pop()
                maps[small]=num
            stack.append(num)
        
        for n in nums1:
            if n in maps:
                output.append(maps[n])
            else:
                output.append(-1)
        return output
            

        