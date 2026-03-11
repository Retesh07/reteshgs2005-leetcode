class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:

        position.sort()
        l=1
        r=(position[-1]-position[0])

        while l<=r:
            mid=(l+r)//2
            if self.canplace(mid,position,m):
                l=mid+1
            else:
                r=mid-1
        return r
    def canplace(self,k,positions,m):
        last=positions[0]
        cntbucket=1
        for i in range(1,len(positions)):
            if abs(positions[i]-last)>=k:
                cntbucket+=1
                last=positions[i]
        if cntbucket>=m:
            return True
        else:
            return False

