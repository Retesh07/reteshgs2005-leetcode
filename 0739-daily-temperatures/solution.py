class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        k=len(temperatures)
        output=[0]*k
        stack=[]
        for index, value in enumerate(temperatures):
            while stack and stack[-1][0]<value:
                stackvalue,stackindx = stack.pop()
                output[stackindx]=(index-stackindx)
            stack.append([value,index])
        return output




            

        