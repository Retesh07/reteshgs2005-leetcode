class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        if sum(matchsticks)%4!=0:
            return False
        n=sum(matchsticks)//4
        
        matchsticks.sort(reverse=True)
        if matchsticks[0]>n:
            return False
        sides=[0,0,0,0]

        def dfs(i):
            if i==len(matchsticks):
                return sides[0]==sides[1]==sides[2]==sides[3]
            
            for side in range(4):
                if sides[side]+matchsticks[i]<=n:
                    sides[side]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    sides[side]-=matchsticks[i]
                if sides[side]==0:
                    break
            return False

        return dfs(0)






        
        