class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash1 = defaultdict(int)
        res = []
        i = 1

        for num in nums:
            hash1[num] = target - num
            if hash1[num] in nums[i:]:
                res.append(nums.index(num))
                res.append(nums.index(hash1[num], i))
                break
            i+=1
        
        return res
                

        