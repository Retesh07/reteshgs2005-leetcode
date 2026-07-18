class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        sums=0
        n=len(nums)
        for i in range(0,n-3):
            if i>0 and nums[i-1]==nums[i]:
                continue
            for j in range(i+1,n-2):
                if j!=i+1 and nums[j-1]==nums[j]:
                    continue
                k=j+1
                l=n-1
                
                while(k<l):
                    sums=nums[i]+nums[j]+nums[k]+nums[l]
                    if sums==target:
                        quad=sorted([nums[i],nums[j],nums[k],nums[l]])
                        result.append(quad)
                        k+=1
                        l-=1
                        while k<l and nums[k-1]==nums[k]:
                            k+=1
                        while k<l and nums[l+1]==nums[l]:
                            l-=1
                    elif sums>target:
                        l-=1
                    else:
                        k+=1
        return result
                
    
          




        