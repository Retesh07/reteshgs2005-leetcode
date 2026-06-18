class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        output=""
        
        for ch in s:
            if ch==']':
                curr=""
                while stack and stack[-1]!='[':
                    curr=stack.pop()+curr
                stack.pop()
                k=""
                while stack and stack[-1].isdigit():
                    k=stack.pop()+k

                curr=int(k)*curr
                stack.append(curr)

            
            else:
                stack.append(ch)
        for m in stack:
            output+=m
        return output
        