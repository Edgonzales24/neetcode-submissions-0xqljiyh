class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = nums.copy()
        heapq.heapify(maxHeap)
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        return maxHeap[0]