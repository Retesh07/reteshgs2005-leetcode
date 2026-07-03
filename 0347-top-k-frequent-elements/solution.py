class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=defaultdict(int)
        freq=[[] for i in range(len(nums)+1)]

        for num in nums:
            a[num]+=1
        res=[]
        for key,value in a.items():

            freq[value].append(key)
        for j in range(len(freq)-1,0,-1):
            for num in freq[j]:
                res.append(num)
                if len(res)==k:
                    return res




        