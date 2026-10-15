class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sums=0
        for i in range(len(nums)):
            sums+=1
            m=1
            h=set()
            h.add(nums[i])
            for j in range(i+1,len(nums)):
                if nums[j] not in h:
                    
    
                    m+=1
                
                sums+=m*m
                h.add(nums[j])
                print(sums)
        return sums

        