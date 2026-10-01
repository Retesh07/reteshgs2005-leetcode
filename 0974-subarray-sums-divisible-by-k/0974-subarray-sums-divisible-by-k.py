class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        r=defaultdict(int)
        r[0]=1
        sums=0
        count=0

        for h in nums:
            sums+=h
            if sums%k in r:
            
                count+=r[sums%k]
            r[sums%k]=r.get(sums%k,0)+1
        return count
       

        