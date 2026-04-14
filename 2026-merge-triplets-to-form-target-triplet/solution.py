class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a,b,c=False,False,False

        for i,j,k in triplets:
            if i<=target[0] and j<=target[1] and k<=target[2]:
                if i==target[0]:
                    a=True
                if j==target[1]:
                    b=True
                if k==target[2]:
                    c=True
        return True if a and b and c == True else False
        