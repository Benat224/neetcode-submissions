class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euclideanDistance(p1, p2):
            return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

        result = []
        heap = [(euclideanDistance(p,[0,0]), p) for p in points]
        heapq.heapify(heap)
        print(heap)
        while k != 0 and len(heap) != 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result