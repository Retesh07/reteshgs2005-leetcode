class Solution:
    def smallestPalindrome(self, s: str) -> str:
        left=""
        mid=""
        maps=Counter(s)
        for ch in "abcdefghijklmnopqrstuvwxyz":
            left+=ch*(maps[ch]//2)
            if maps[ch]%2==1:
                mid+=ch
        right=""
        for i in range(len(left)-1,-1,-1):
            right+=left[i]
  
        return left+mid+right

        