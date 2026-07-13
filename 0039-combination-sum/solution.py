class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def rec(index,total,temp):
            if total==target:
                res.append(list(temp))
                return
            if total>target:
                return
            for i in range(index,len(candidates)):
                
                temp.append(candidates[i])
                rec(i,total+candidates[i],temp)
                temp.pop()
                



        rec(0,0,[])
        return res