class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maximum_amount = 0;

        while l < r:
            height = min(heights[l], heights[r])
            width = r - l
            amount = height * width
            
            maximum_amount = max(amount, maximum_amount)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        
        return maximum_amount