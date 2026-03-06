from collections import defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

       
        parents = defaultdict(list)

        current = {beginWord}
        found = False

        while current and not found:
           
            wordSet -= current

            next_level = set()

            for word in current:
                word_chars = list(word)

                for i in range(len(word_chars)):
                    original = word_chars[i]

                    for c in "abcdefghijklmnopqrstuvwxyz":
                        word_chars[i] = c
                        new_word = "".join(word_chars)

                        if new_word not in wordSet:
                            continue

                        if new_word == endWord:
                            found = True

                        next_level.add(new_word)
                        parents[new_word].append(word)

                    word_chars[i] = original

            current = next_level

        if not found:
            return []

        ans = []
        path = []

        def dfs(word):
            path.append(word)

            if word == beginWord:
                ans.append(path[::-1])
            else:
                for parent in parents[word]:
                    dfs(parent)

            path.pop()

        dfs(endWord)
        return ans