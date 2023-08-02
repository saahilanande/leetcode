class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while(len(stones))>1:   
            val1 = heapq.heappop(stones)
            val2 = heapq.heappop(stones)

            if val1 == val2:
                heapq.heappush(stones,0)
            else:
                heapq.heappush(stones,val1-val2)
        
        return abs(stones[0])
        