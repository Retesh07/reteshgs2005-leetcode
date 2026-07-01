class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        start, end = 0, 0
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
        
        for i in range(len(s)):
            
            l, r = expand(i, i)
            if r - l > end - start:
                start, end = l, r
            
           
            l, r = expand(i, i + 1)
            if r - l > end - start:
                start, end = l, r
        
        return s[start:end + 1]