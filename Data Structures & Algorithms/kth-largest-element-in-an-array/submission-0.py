class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]

        heapq.heapify(nums)
        for i in range(k):
            result = heapq.heappop(nums)
        return -result