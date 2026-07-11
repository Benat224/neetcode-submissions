class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        aux = lambda stones: [-x for x in stones]
        heap = aux(stones)
        heapq.heapify(heap)
        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)
            
            if x > y:
                heapq.heappush(heap, -(x-y))
        
        if len(heap) == 0:
            return 0
        else:
            return -heap[0]

