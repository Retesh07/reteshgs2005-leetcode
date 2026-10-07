class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count=0
        stack=[0]
        for c in s:
            if c=='(':
                stack.append(0)
            else:
                val=stack.pop()
                if val==0:
                    val=1
                else:
                    val=2*val
                stack[-1]+=val
                
        return stack[0]

        