class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return sum(cost)
    
        
        cost.sort(reverse=True)
        sums=0
        for i in range(len(cost)):
            if (i+1)%3==0:
                continue
            sums+=cost[i]
        return sums



        


        