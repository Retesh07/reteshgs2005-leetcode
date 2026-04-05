class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        i=len(a)-1
        j=len(b)-1
        carry=0

        while i>=0 or j>=0 or carry:
            carry+=(int(a[i]) if i>=0 else 0)+(int(b[j]) if j>=0 else 0)

            res.append(str(carry%2))
            carry//=2
            i-=1
            j-=1
        return ''.join(res[::-1])


        