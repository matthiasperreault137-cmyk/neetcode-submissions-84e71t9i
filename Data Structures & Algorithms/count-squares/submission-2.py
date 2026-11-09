class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point):
        key = (point[0], point[1])
        self.points[key] = self.points.get(key, 0) + 1

    def count(self, point: List[int]) -> int:
        total = 0
        for i in range(1, 1001):
            x = point[0] + i
            y = point[1] + i
            val = self.points.get((x,y), 0)
            if val != 0:
                if self.points.get((point[0], y), 0) != 0 and self.points.get((x, point[1])) != 0:
                    total += val * self.points.get((point[0], y), 0) * self.points.get((x, point[1]), 0)       
        for i in range(1, 1001):
            x = point[0] + i
            y = point[1] - i
            val = self.points.get((x,y), 0)
            if val != 0:
                if self.points.get((point[0], y), 0) != 0 and self.points.get((x, point[1])) != 0:
                    total += val * self.points.get((point[0], y), 0) * self.points.get((x, point[1]), 0) 
        for i in range(1, 1001):
            x = point[0] - i
            y = point[1] + i
            val = self.points.get((x,y), 0)
            if val != 0:
                if self.points.get((point[0], y), 0) != 0 and self.points.get((x, point[1])) != 0:
                    total += val * self.points.get((point[0], y), 0) * self.points.get((x, point[1]), 0) 
        for i in range(1, 1001):
            x = point[0] - i
            y = point[1] - i
            val = self.points.get((x,y), 0)
            if val != 0:
                if self.points.get((point[0], y), 0) != 0 and self.points.get((x, point[1])) != 0:
                    total += val * self.points.get((point[0], y), 0) * self.points.get((x, point[1]), 0)
        return total