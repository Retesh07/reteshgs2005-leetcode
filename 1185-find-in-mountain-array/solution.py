# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l,r=0,mountainArr.length()-1
        peak=0

        while l<r:
            mid=(l+r)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                l=mid+1
            else:
                r=mid
        peak=l
        if mountainArr.get(peak)==target:
            return peak
        n=0
        m=self.binarysearchasc(target,mountainArr,0,peak-1)
        if m==-1:
            n=self.binarysearchdesc(target,mountainArr,peak+1,mountainArr.length()-1)
            if n==-1:
                return -1
            else:
                return n
        else:
            return m
    def binarysearchasc(self,target:int,mountainArr:'MountainArray',l:int,r:int)->int:
        while l<=r:
            mid=(l+r)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                r=mid-1
            else:
                l=mid+1
        return -1
    def binarysearchdesc(self,target:int,mountainArr:'MountainArray',l:int,r:int)->int:
        while l<=r:
            mid=(l+r)//2
            if mountainArr.get(mid)==target:
                return mid
            elif mountainArr.get(mid)>target:
                l=mid+1
            else:
                r=mid-1
        return -1
        