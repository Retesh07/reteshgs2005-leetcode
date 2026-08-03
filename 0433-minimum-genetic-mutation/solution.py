class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        check=set(bank)
        if endGene not in check:
            return -1
        q=deque()
        q.append((startGene,0))
        visited=set()
        while q:
            g,steps=q.popleft()
            if g==endGene:
                return steps
            for i in range(8):
                for ch in ['A','C','G','T']:
                    if ch==g[i]:
                        continue
                    nexts=g[:i]+ch+g[i+1:]
                    if nexts in check and nexts not in visited:
                        visited.add(nexts)
                        q.append((nexts,steps+1))
        return -1

        