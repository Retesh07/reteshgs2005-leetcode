class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mp1=defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                mp1[n1+n2]+=1

        cnt=0
        for n3 in nums3:
            for n4 in nums4:
                n5=n3+n4
                n6=-n5
                if n6 in mp1:
                    cnt+=mp1[n6]
        return cnt

        
        