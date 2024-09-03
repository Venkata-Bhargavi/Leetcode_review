import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        for i, f in count.items():
            heapq.heappush(heap, (f, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for f, num in heap]
