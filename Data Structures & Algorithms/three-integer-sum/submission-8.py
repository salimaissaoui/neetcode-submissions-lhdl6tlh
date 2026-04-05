class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

   

        for i in range(len(nums)):
            for j in range(len(nums)):
                k = len(nums) - 1
                while j < k:
                    if j != i and k != i:
                        if nums[i] == -(nums[j] + nums[k]):
                            temp = []
                            temp.append(nums[i])
                            temp.append(nums[j])
                            temp.append(nums[k])
                            temp.sort()
                            if temp  not in res:
                                res.append(temp)
                                temp = []
                    
                    k-=1


        return res

