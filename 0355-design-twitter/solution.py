class Twitter:

    def __init__(self):
        self.count=0
        self.followid=defaultdict(set)
        self.postid = defaultdict(list)


        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postid[userId].append([self.count,tweetId])
        self.count-=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

       
        self.followid[userId].add(userId)

     
        for followee in self.followid[userId]:
            if followee in  self.postid:
                
                index = len(self.postid[followee]) - 1

                count, tweetId = self.postid[followee][index]

                heapq.heappush(
                    minHeap,
                    [count, tweetId, followee, index]
                )

        while minHeap and len(res) < 10:
            count, tweetId, followee, index = heapq.heappop(minHeap)

            res.append(tweetId)

          
            if index > 0:
                count, tweetId = self.postid[followee][index - 1]

                heapq.heappush(
                    minHeap,
                    [count, tweetId, followee, index - 1]
                )

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followid[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followid[followerId]:
            self.followid[followerId].remove(followeeId)

        
