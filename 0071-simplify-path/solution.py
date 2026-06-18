class Solution:
    def simplifyPath(self, path: str) -> str:
        parts=path.split('/')
        stack=[]
        for ch in parts:
            if ch=='' or ch=='.':
                continue
            elif ch=='..':
                if stack:
                    stack.pop()
            else:
                stack.append(ch)
        return '/' + '/'.join(stack)

        