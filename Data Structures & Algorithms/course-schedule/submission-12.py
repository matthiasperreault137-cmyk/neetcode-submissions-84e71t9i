class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        map = {}
        acquired = set()
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in map:
                map[prerequisites[i][0]] = []
            map[prerequisites[i][0]].append(prerequisites[i][1])
        def DFS(val, path):
            if val in path:
                return False
            if val not in map or val in acquired:
                if val not in acquired:
                    acquired.add(val)
                return True
            path.add(val)
            requisites = map[val]
            for req in requisites:
                if req in acquired:
                    continue
                if not DFS(req, path):
                    return False
            path.remove(val)
            acquired.add(val)
            return True

        for i in range(numCourses):
            path = set()  
            if not DFS(i, path):
                return False
        return True

