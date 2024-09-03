class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            current_height = min(heights[l], heights[r])
            current_width = r - l
            current_area = current_height * current_width
            res = max(res, current_area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res



