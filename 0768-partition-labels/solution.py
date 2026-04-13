class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap={ch:i for i,ch in enumerate(s)}
        res=[]
        start=0 
        end=0

        for i,ch in enumerate(s):
            end=max(end,hashmap[s[i]])
            if i==end:
                res.append(end-start+1)
                start=i+1

        

        
        return res
        