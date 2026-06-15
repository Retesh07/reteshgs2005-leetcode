class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights),sum(weights)
        res = r

        while l <= r:
            k = (l + r) // 2

            totalweights = 0
            totaldays=1
            for p in weights:
                if totalweights+p>k:
                    totaldays+=1
                    totalweights=0
            

                totalweights+=p
                


                
            if totaldays <= days:
                res = k
                r = k - 1
            else:
                l = k + 1
        return res
        