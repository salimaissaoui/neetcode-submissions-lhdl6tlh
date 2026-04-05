class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        difference = defaultdict(int)

        for i in range(len(numbers)):
            difference[numbers[i]] = target - numbers[i]
        
        for key, num in difference.items():
            if key + num == target and num in numbers and numbers.index(key) != numbers.index(num) :
                return [numbers.index(key) + 1, numbers.index(num) + 1] 
        