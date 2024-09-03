########
#brute force O(nlogn)
#########
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)

        return self.nums[self.k - 1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)




######
#using heapq
#######

import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.min_heap = []
        # Initialize the heap with the first k elements or less if nums has fewer elements
        for num in nums:
            self.add(num)

    def add(self, val):
        # If heap has fewer than k elements, just add the new value
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            # If heap has k elements, push the new value and remove the smallest
            if val > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, val)
        # Return the Kth largest element (root of the heap)
        return self.min_heap[0]


# Example usage
k = 3
nums = [4, 5, 8, 2]
kthLargest = KthLargest(k, nums)

print(kthLargest.add(3))  # Returns 4 (the 3rd largest element)
print(kthLargest.add(5))  # Returns 5 (the 3rd largest element)
print(kthLargest.add(10))  # Returns 5 (the 3rd largest element)
print(kthLargest.add(9))  # Returns 8 (the 3rd largest element)
print(kthLargest.add(4))  # Returns 8 (the 3rd largest element)





