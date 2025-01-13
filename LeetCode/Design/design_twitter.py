class Twitter:
    def __init__(self):
        # Initialize user_follow_map to keep track of the users each user follows.
        # Default is an empty set for each user.
        self.user_follow_map = defaultdict(set)

        # Initialize tweets to store tweets by each user.
        # Each tweet is stored as (timestamp, tweet_id).
        self.tweets = defaultdict(list)

        # Global timestamp to order tweets chronologically.
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Posts a new tweet by the user.
        """
        # Add the tweet to the user's tweet list with the current timestamp.
        self.tweets[userId].append((self.timestamp, tweetId))

        # Increment the global timestamp to ensure chronological order.
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Retrieves the 10 most recent tweet IDs in the user's news feed.
        """
        # Get the list of users the user is following, including themselves.
        followed_users = self.user_follow_map[userId] | {userId}

        # Create a min-heap to keep track of the most recent tweets.
        # Max size of heap will be 10 to ensure only top 10 tweets are retrieved.
        heap = []
        for user in followed_users:
            for tweet in self.tweets[user]:
                heapq.heappush(heap, tweet)
                # Ensure the heap only contains the 10 most recent tweets.
                if len(heap) > 10:
                    heapq.heappop(heap)

        ans = []
        while heap:
            _ ,tweet_id = heapq.heappop(heap)
            ans.append(tweet_id)
        ans.reverse()
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follows a user.
        """
        # Add the followee to the follower's set of followed users.
        self.user_follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Unfollows a user if the user is in the follower's followed set.
        """
        # Remove the followee from the follower's set of followed users.
        # Check to avoid errors if the followee is not in the set.
        self.user_follow_map[followerId].discard(followeeId)
