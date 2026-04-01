class TimeMap:

    def __init__(self):
        self.store = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        right = len(self.store[key]) - 1
        left = 0
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if self.store[key][mid][1] <= timestamp:
                res = self.store[key][mid][0]
                left = mid + 1    
            else:
                right = mid - 1 

        return res

