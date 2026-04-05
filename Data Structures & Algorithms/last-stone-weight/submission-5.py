class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            print(x,y)
            if x == y:
                continue
            else:
                heapq.heappush(stones, x - y)
        
        
        return -heapq.heappop(stones) if stones else 0

        
