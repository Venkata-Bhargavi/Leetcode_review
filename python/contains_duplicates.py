######
# extra space complexity , brute force
########


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique_count = len(set(nums))
        return unique_count < len(nums)




#######
### early return , best case O(1) if foud early
# ######



def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
