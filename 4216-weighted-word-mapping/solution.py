class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=""
        for word in words:
            total=0
            for ch in word:
                total+=weights[ord(ch)-ord('a')]
            rem=total%26
            res+=(chr(ord('z')-rem))
        return res
            


