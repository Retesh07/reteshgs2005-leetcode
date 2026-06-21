class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for value in tokens:
            if value=='+' or value=='-' or value=='*' or value=='/':
                v1=stack.pop()
                v2=stack.pop()
                if value=='+':
                    stack.append(v1+v2)
                elif value=='-':

                    stack.append(v2-v1)
                elif value=='*':
                    stack.append(v2*v1)
                else:

                    stack.append(int(v2/v1))
            else:
                stack.append(int(value))
        return stack[-1]