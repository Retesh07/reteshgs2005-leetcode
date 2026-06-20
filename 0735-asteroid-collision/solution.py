class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s1=[]
        for value in asteroids:
            while s1 and value<0 and s1[-1]>0:
                d=value+s1[-1]
                if d>0:
                    value=0
                elif d<0:
                    s1.pop()
                else:
                    s1.pop()
                    value=0
            if value:
                s1.append(value)
        return s1

        