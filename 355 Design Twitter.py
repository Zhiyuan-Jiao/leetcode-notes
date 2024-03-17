class Twitter:

    def __init__(self):
        self.userTweets = defaultdict(list)  # userId : [[time1, tweetId1], [time2, tweetId2], ...]
        self.userFollows = defaultdict(set)  # userId : set(userId1, userId2, ...)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.userTweets[userId].append([-self.time, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = self.userTweets[userId].copy()
        for user in self.userFollows[userId]:
            tweets.extend(self.userTweets[user])
        heapq.heapify(tweets)
        res = []
        while tweets and len(res) < 10:
            res.append(heapq.heappop(tweets)[1])
        return res
        
        # Time complexity: O(n + klogn), k = 10

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userFollows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)