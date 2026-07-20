import heapq

class KthLargest:

    def __init__(self, k, nums):
        self.k = k

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)

        self.heap = nums

    def add(self, val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]