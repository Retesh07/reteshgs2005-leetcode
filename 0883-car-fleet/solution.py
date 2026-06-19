class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s=sorted(list(zip(position,speed)), key=lambda x:x[0], reverse=True)
        last_time=0
        fleet=0
        for i in range(len(s)):
            time = (target-s[i][0])/s[i][1]
            if time>last_time:
                fleet+=1
                last_time=time
        return fleet

    