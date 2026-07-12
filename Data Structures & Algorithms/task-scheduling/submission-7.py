class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = defaultdict(int)
        for elem in tasks:
            mp[elem] += 1
    
        heap1 = [(mp[elem]*(-1), elem) for elem in mp]
        heap2 = []
        heapq.heapify(heap1)
        heapq.heapify(heap2)
        counter = 0
        while len(heap1) != 0 or len(heap2) != 0:
            if len(heap1) == 0:
                nxt = heap2[0][0]
                counter = nxt
            while len(heap2) != 0 and heap2[0][0] == counter:
                _, count, elem = heapq.heappop(heap2)
                heapq.heappush(heap1, (count, elem))
            print(heap1)
            count, elem = heapq.heappop(heap1)
            if -count > 1:
                heapq.heappush(heap2, (counter + n + 1, count+1, elem))
            counter += 1
            
        return counter