class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        leftmax=[0]*n
        rightmax=[0]*n
        
        leftmax[0]=height[0]
        rightmax[n-1]=height[n-1]
        sol=0

        for i in range(1,n,1):
            leftmax[i]=max(height[i],leftmax[i-1])
        for j in range(n-2,-1,-1):
            rightmax[j]=max(rightmax[j+1],height[j])
        for k in range(n):
            sol+=min(leftmax[k],rightmax[k])-height[k]
        return sol

        
        