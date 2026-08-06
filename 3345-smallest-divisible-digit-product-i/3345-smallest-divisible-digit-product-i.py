class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        i=n
        for i in range(i,101):
            c=str(i)
      
            mul=1
            for j in range(len(c)):
                mul*=int(c[j])
            if mul%t==0:
                return int(c)
        return -1
        