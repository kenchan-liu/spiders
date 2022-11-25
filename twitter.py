class Twitter:

    def __init__(self):
        self.tweet = {}
        self.follow = {}
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId in self.tweet:
            self.tweet[userId].append(tweetId)
        else:
            self.tweet[userId] = [tweetId]


    def getNewsFeed(self, userId: int):
        temp = self.tweet[userId]
        out = []
        while(temp):
            out.append(temp.pop())
        return out

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow:
            self.followe[followeeId].append(followeeId)
        else:
            self.follow[followerId] = [followeeId]


    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow[followerId].remove(followeeId)
T = Twitter()
T.postTweet(2,3)