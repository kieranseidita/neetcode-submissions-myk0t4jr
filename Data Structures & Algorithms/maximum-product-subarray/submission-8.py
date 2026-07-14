class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Step 1: Create 3 subarrays: curr_sub, max_sub, & min_sub
        curr_sub = nums[0]
        min_sub = nums[0]
        max_sub = nums[0]

        #Step 2: We need to now go through each value that is contained in our array
        for i in range(1,len(nums)):
            #Step 3: We will check if our result is greater than our max_sub
            candidates = (nums[i], curr_sub * nums[i], min_sub * nums[i])

            #Step 6: We then need to truly find out if this value
            curr_sub = max(candidates)
                
            #Step 5: We also need to update our minimum to be the opposite value of this
            min_sub = min(candidates)

            #Step 7: Find mininum of max_sub & curr_sub
            max_sub = max(max_sub,curr_sub)
        
        # Default Case: We will return our max sub for our maximum product subarray
        return max_sub