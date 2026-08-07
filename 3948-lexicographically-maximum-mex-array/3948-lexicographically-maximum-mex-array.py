class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:
        freq=defaultdict(int)
        for j in range(len(nums)):
            freq[nums[j]]+=1

        i=0
        n=len(nums)
        res=[]
        while i<n:
            target=0
            while freq[target]>0:
                target+=1
            if target==0:
                return res + [0] * (n - i)
            seen=set()
            while i<n:
                number=nums[i]
                if number<target:
                    seen.add(number)
                freq[number]-=1
                i+=1
                if len(seen)==target:
                    res.append(target)
                    break
        return res
                    
            


       
        
        