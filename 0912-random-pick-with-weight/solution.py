class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0

        for weight in w:
            total += weight
            self.prefix.append(total)

        self.total = total

    def pickIndex(self) -> int:
       
        target = random.randint(1, self.total)
        for i in range(len(self.prefix)):
            if target<=self.prefix[i]:
                return i

   
        