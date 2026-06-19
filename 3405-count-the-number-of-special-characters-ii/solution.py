class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower={}
        upper={}
        for i, ch in enumerate(word):
            if ch.islower():
                lower[ch]=i
            else:
                l=ch.lower()
                if l not in upper:
                    upper[l]=i
        count=0
        for ch in upper:
            if ch in lower and upper[ch]>lower[ch]:
                count+=1
        return count