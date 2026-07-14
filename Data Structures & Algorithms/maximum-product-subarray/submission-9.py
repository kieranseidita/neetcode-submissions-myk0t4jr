class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Step 1: Create our 3 subarrays for this problems
        curr_sub = nums[0]
        min_sub = nums[0]
        max_sub = nums[0]

        #Step 2: We will go through each number that is contained within our array
        for i in range(1, len(nums)):
            #Step 3: Create our candidates
            candidates = (nums[i], curr_sub * nums[i], min_sub * nums[i])

            #Step 4: We need to find maximum product of our candidates and make it the current subarray
            curr_sub = max(candidates)

            #Step 5: We need to find minimum product of our candidates
            min_sub = min(candidates)

            #Step 6: Now we need to determine max subarray between max_sub and curr_sub
            max_sub = max(max_sub,curr_sub)
        
        #Return our max_sub
        return max_sub
