class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        res=[0]*(len(num1)+len(num2))

        for i in range(len(num1)-1,-1,-1):
            d1=ord(num1[i])-ord('0')
            for j in range(len(num2)-1,-1,-1):
                
                d2=ord(num2[j])-ord('0')

                result=res[i+j+1]+d1*d2
                res[i+j+1]=result%10
                res[i+j]+=result//10

        i = 0
        while i < len(res)-1 and res[i] == 0:
            i += 1

        return ''.join(map(str, res[i:]))
