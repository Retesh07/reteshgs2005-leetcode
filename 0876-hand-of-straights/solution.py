class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize:
            return False
            

        count=Counter(hand)

        for num in sorted(count):
            freq=count[num]

            if freq>0:
                for nxt in range(num,num+groupSize):
                    if count[nxt]<freq:
                        return False
                    count[nxt]-=freq
        return True
        