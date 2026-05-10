class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        mp=defaultdict(list)

        for word in wordList:
            for i in range(len(word)):
                pattern=word[:i]+"*"+word[i+1:]
                mp[pattern].append(word)
        visited=set()
        visited.add(beginWord)
        q=deque()
        q.append(beginWord)
        res=1


        while q:
            for k in range(len(q)):
                w=q.popleft()

                if w==endWord:
                    return res
                for i in range(len(w)):
                    pattern=w[:i]+"*"+w[i+1:]
                    for neig in mp[pattern]:
                        if neig not in visited:
                            visited.add(neig)
                            q.append(neig)
            res+=1
        return 0
            
            



        