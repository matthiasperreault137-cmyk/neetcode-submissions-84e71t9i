class MaxHeap:
    def __init__(self, array):
        self.heap = self.heapifyAll(array)

    def push(self, item):
        self.heap.append(item)
        i = len(self.heap) - 1
        while i > 0:
            p = (i - 1) // 2
            if self.heap[i][0] > self.heap[p][0]:
                self.heap[i], self.heap[p] = self.heap[p], self.heap[i]
                i = p
            else:
                break

    def pop(self):
        item = self.heap[0]
        last = self.heap.pop()
        if self.heap:
            self.heap[0] = last
            self.heapifyDown(0, self.heap)
        return item

    def heapifyDown(self, i, array):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        if left < len(array) and array[left][0] > array[largest][0]:
            largest = left
        if right < len(array) and array[right][0] > array[largest][0]:
            largest = right
        if largest == i:
            return
        array[i], array[largest] = array[largest], array[i]
        self.heapifyDown(largest, array)

    def heapifyAll(self, array):
        copy = array.copy()
        cutoff = (len(copy) // 2) - 1
        for i in range(cutoff, -1, -1):
            self.heapifyDown(i, copy)
        return copy

    def peek(self):
        return self.heap[0]


class User:
    def __init__(self, id):
        self.id = id
        self.followed = set()
        self.tweets = []


class Twitter:
    def __init__(self):
        self.users = {}
        self.time = 0

    def _getUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._getUser(userId)
        user.tweets.append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        feed = []
        heap = MaxHeap([])

        user = self._getUser(userId)
        sources = user.followed | {userId}

        for uid in sources:
            u = self.users[uid]
            if u.tweets:
                nextIdx = 1
                ts, tid = u.tweets[-nextIdx]
                heap.push((ts, tid, (uid, nextIdx)))

        while len(feed) < 10 and heap.heap:
            ts, tid, (uid, idx) = heap.pop()
            feed.append(tid)
            u = self.users[uid]
            nextIdx = idx + 1
            if nextIdx <= len(u.tweets):
                ts2, tid2 = u.tweets[-nextIdx]
                heap.push((ts2, tid2, (uid, nextIdx)))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self._getUser(followerId)
        self._getUser(followeeId)
        self.users[followerId].followed.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users and followeeId in self.users[followerId].followed:
            self.users[followerId].followed.remove(followeeId)