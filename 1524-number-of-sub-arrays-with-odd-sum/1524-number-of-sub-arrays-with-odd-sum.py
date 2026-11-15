class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        odd=0
        even=1
        sums=0
        modulo=10**9+7

        ans=0
        for i in range(len(arr)):
            sums+=arr[i]
            if sums%2==0:
                ans+=odd
                even+=1
            
            else:
                ans+=even
                odd+=1
        return ans%modulo



        