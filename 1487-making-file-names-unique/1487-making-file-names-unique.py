class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        
        visited=set()
        next_k={}

        res=[]
        for name in names:
            if name not in visited:

                visited.add(name)
                next_k[name]=1
                res.append(name)
        
            else:
                k=next_k[name]
                while f"{name}({k})" in visited:
                    k+=1
                res.append(f"{name}({k})")
                next_k[name]=k+1
                next_k[f"{name}({k})"]=1
                visited.add(f"{name}({k})")
        return res

      





            
        