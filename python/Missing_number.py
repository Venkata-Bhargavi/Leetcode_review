class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # find the sum of all nums in the range
        n = len(nums)
        sum_of_nums = (n * (n + 1)) // 2
        sum_of_lis = sum(nums)
        return sum_of_nums - sum_of_lis
