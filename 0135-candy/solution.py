class Solution:
    def candy(self, ratings: List[int]) -> int:

        arr=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                arr[i]=arr[i-1]+1
        for j in range(len(ratings)-2,-1,-1):
            if ratings[j]>ratings[j+1]:
                arr[j]=max(arr[j],arr[j+1]+1)
        return sum(arr)
        