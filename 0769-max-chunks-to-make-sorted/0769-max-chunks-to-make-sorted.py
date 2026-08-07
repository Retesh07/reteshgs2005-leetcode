class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        maxi=float("-inf")
        result=0

        for i in range(len(arr)):
            maxi=max(arr[i],maxi)
            if i==maxi:
                result+=1
        return result
