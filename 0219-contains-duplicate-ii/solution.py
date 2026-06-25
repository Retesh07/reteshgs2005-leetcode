class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash=defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in hash:
                hash[nums[i]]=i
            else:
                if i-hash[nums[i]]<=k:
                    
                    return True
                hash[nums[i]]=i
                    
        return False        
     

    

        