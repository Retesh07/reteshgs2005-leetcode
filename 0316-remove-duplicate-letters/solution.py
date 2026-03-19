class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)    
        stack = []
        inStack = set()    
        for ch in s:
            freq[ch] -= 1
            if ch in inStack:
                continue

            while stack and stack[-1] > ch and freq[stack[-1]] > 0:
                removed = stack.pop()
                inStack.remove(removed)

          
            stack.append(ch)
            inStack.add(ch)

        return "".join(stack)