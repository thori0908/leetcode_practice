import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        reversed_stones = [stone * -1 for stone in stones]
        heapq.heapify(reversed_stones)

        while len(reversed_stones) > 1:
            first_heaviest = heapq.heappop(reversed_stones)
            second_heaviest = heapq.heappop(reversed_stones)
            if first_heaviest != second_heaviest:
                heapq.heappush(reversed_stones, first_heaviest - second_heaviest)

        return -heapq.heappop(reversed_stones) if reversed_stones else 0