class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:

        nums3=[]
        for i in range(len(nums1)):
            nums3.append(abs(nums1[i]-nums2[i]))
        freq=[]
        k=k1+k2
        if sum(nums3) <= k:
            return 0
        max_diff = max(nums3)
        freq = [0] * (max_diff + 1)

        for d in nums3:
            freq[d] += 1
        for m in range(max_diff,0,-1):
            count=freq[m]

            c=min(k,count)
            freq[m]-=c
            freq[m-1]+=c
            k-=c
        return sum(d * d * count for d, count in enumerate(freq))
        