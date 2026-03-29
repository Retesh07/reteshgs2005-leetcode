class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        m=sorted(arr)
        mp={}
        
        output=[]
        k=1

        for i in range(len(m)):
            if m[i] not in mp.keys():

            
                mp[m[i]]=k
                k+=1
     

    
        for j in range(len(arr)):
            output.append(mp[arr[j]])
        return output

        