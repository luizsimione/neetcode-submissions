class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        maxWater = 0

        while left < right:
            height = min(heights[left], heights[right])
            width = right - left


            currArea = height * width
            maxWater = max(currArea, maxWater)

            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
           

        return maxWater
            # if right is bigger than left, left increment vice versa
            # if current is greatest seen, update
            