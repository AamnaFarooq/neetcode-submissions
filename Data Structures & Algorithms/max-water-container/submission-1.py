class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #need to find max area
        #move one pointer left
        #move one pointer right
        #subtract them to get width
        #multiply by minimum height to get area

        left = 0 
        right = len(heights) - 1
        max_area = 0

        while left < right:
            width = abs(left - right)
            height = min(heights[left], heights[right])
            area = width * height 
            max_area = max(area, max_area)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

            



            

