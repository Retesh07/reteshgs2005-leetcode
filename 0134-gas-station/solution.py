class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        currtank=0
       
        diff=0
        start=0

        for i in range(len(gas)):
            
            diff=gas[i]-cost[i]
            total+=diff
            currtank+=diff
            
            if currtank<0:
                currtank=0
                start=i+1
        return start if total>=0 else -1


        