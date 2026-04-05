class MedianFinder:

    def __init__(self):
        self.nums = []
    

    def addNum(self, num: int) -> None:
        left, right = 0, len(self.nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.nums[mid] == num:
                self.nums.insert(mid , num)
                return
            elif self.nums[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        self.nums.insert(left, num)
        

    def findMedian(self) -> float:
        mid = len(self.nums) // 2

        return (self.nums[mid] + self.nums[mid - 1]) / 2 if len(self.nums) % 2 == 0 else self.nums[mid]
        