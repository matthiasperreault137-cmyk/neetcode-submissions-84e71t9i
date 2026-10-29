import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        matrix = []
        for _ in range(n + 1):
            matrix.append([])
        for edge in times:
            u = edge[0]
            neighbor = edge[1]
            w = edge[2]
            matrix[u].append((neighbor,w))
        def djikstra(start):
            fuckyou = [9999] * (n + 1)
            path = [None] * (n + 1)
            visited = set()


            fuckyou[start] = 0
            heap = []
            heapq.heappush(heap, (fuckyou[start], start))

            while heap:
                popVal = heapq.heappop(heap)
                node = popVal[1]

                if node in visited:
                    continue
                
                visited.add(node)

                for v in matrix[node]:
                    val = v[1]
                    neighbor = v[0]

                    if val + fuckyou[node] < fuckyou[neighbor]:
                        fuckyou[neighbor] = fuckyou[node] + val
                        path[neighbor] = node
                        heapq.heappush(heap, (fuckyou[neighbor], neighbor))
            return fuckyou, path
        fuckyou2, path2 = djikstra(k)
        result = 0
        for i in range(1,n + 1):
            result = max(fuckyou2[i], result)
        if result > 999:
            return -1
        return result