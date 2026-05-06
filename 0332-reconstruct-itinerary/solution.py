class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        mp = defaultdict(list)
        for src,dst in tickets:
            mp[src].append(dst)
        for n in mp.values():
            n.sort(reverse=True)
        res=[]
        
        
        def dfs(i):

            while mp[i]:
                
                k=mp[i].pop()
                dfs(k)
            res.append(i)
            
        
        dfs("JFK")
        return res[::-1]
            


        