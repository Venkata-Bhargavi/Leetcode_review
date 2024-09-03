class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i,num in enumerate(nums):
            other = target - num
            if other in num_dict:
                return [num_dict[other], i]
            num_dict[num] = i

        return []