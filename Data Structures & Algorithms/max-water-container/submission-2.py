class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0

        i = 0
        j = len(heights) - 1

        while i < j:

            height = min(heights[i], heights[j])
            width = j - i
            if height * width > max_area:
                max_area = height * width

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1




        return max_area