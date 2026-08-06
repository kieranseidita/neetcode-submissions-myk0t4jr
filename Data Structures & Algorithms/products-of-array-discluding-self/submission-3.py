class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      #Step 1: Create 3 variables: output, prefix, postfix
      output = [1] * len(nums)
      prefix = 1
      postfix = 1

      #Step 2: Go and update our output array to reflect the prefix
      for i in range(0, len(nums)):
        output[i] = prefix
        prefix *= nums[i]
      
      #Step 3: Another for postfix
      for i in range(len(nums) - 1, -1, -1):
        output[i] = output[i] * postfix
        postfix *= nums[i]
      

      #Default Case: Returning the output array
      return output


    