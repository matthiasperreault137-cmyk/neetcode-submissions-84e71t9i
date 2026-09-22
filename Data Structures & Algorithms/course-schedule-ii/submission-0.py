class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = {}
        acquired = set()
        result = []
        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in map:
                map[prerequisites[i][0]] = []
            map[prerequisites[i][0]].append(prerequisites[i][1])
        def DFS(val, path, results):
            if val in path:
                return False
            if val not in map or val in acquired:
                if val not in acquired:
                    acquired.add(val)
                    results.append(val)
                return True
            path.add(val)
            requisites = map[val]
            for req in requisites:
                if req in acquired:
                    continue
                if not DFS(req, path, results):
                    return False
            path.remove(val)
            acquired.add(val)
            results.append(val)
            return True

        for i in range(numCourses):
            path = set()  
            if not DFS(i, path,result):
                return []
        return result
