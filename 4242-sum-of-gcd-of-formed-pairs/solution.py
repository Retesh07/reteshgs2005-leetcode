class Solution:
    def gcdSum(self, nums: list[int]) -> int:

        prefixgrid=[]
        maxi=nums[0]

        for num in nums:
            maxi=max(maxi,num)
            prefixgrid.append(self.gcd(num,maxi))

        prefixgrid.sort()
        output=0
        i=0
        j=len(prefixgrid)-1

        while i<j:
            output+=(self.gcd(prefixgrid[i],prefixgrid[j]))
            i+=1
            j-=1
        return output
    def gcd(self,a,b):
        if a<b:
            a,b=b,a
        if b==0:
            return a
        return self.gcd(b,a%b)

        