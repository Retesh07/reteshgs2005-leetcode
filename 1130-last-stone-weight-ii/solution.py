class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        if total%2==0:
            r=0
        else:
            r=1
        target = total//2
        dp=set()
        dp.add(0)


        for stone in stones:
            newset=set(dp)

            for i in dp:
                val=i+stone
                if val==target:
                    if r==0:
                        return 0
                    else:
                        return 1
                    
                else:
                    if val<target:
                        newset.add(val)
            dp=newset
        return total-2*(max(dp))
        