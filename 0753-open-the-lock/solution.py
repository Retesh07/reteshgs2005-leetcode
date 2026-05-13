class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited=set(deadends)
        if "0000" in visited:
            return -1
        if "0000"==target:
            return 0

        q=deque()
        q.append("0000")
        steps=0
        while q:
            steps+=1
            for _ in range(len(q)):
                lock=q.popleft()

                for i in range(4):
                    for j in [1,-1]:
                        t=str((int(lock[i])+j+10)%10)
                        newlock=lock[:i]+t+lock[i+1:]
                        if newlock in visited:
                            continue
                        if newlock==target:
                            return steps
                        q.append(newlock)
                        visited.add(newlock)
        return -1
                    




        