class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mp = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
        }
        res=[]
        
        def dfs(combinations,nextdigits):
            if len(nextdigits)==0:
                res.append(combinations)
               
            else:
                for letter in mp[nextdigits[0]]:
                    dfs(combinations+letter,nextdigits[1:])
        



        dfs("",digits)
        return res




        