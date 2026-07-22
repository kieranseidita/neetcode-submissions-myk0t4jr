class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Step 1: Create our 2 pointers for our problems and create the variable for the max_area
        left = 0
        right = len(heights) - 1
        max_area = 0

        #Step 2: We need to create a while loop when tracking the pointers
        while left < right:
            #Step 3: We will need to calculate the width and our height for this value
            height = min(heights[left],heights[right])
            width = right - left

            #Step 4: We need to create our curr_max_area and then update our max_area based on the value
            curr_max_area = height * width

            #Step 5: We need to then update our max_area based on everything
            max_area = max(curr_max_area, max_area)

            #Step 6: We need to add a conditions to compare the heights, is left pointer is bigger, then we will right pointer, if not we will move left pointer
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        # Default Case: We need to return our max area
        return max_area