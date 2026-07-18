class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      #Step 1: We will create an output array and two pointers: prefix and postfix
      output = [1] * len(nums)
      prefix = 1
      postfix = 1

      #Step 2: We need to go through all the numbers that are in here first iterate forwards
      for i in range(0,len(nums)):
        #Step 3: We need to add prefix to our output
        output[i] = prefix

        #Step 3: We need to then multiply 
        prefix *= nums[i]

      #Step 4: We then need to go through the array backwards
      for i in range(len(nums)-1,-1,-1):
        #Step 5: We then need to update our output values
        output[i] = output[i] * postfix

        #Step 6: We then need to update our postfix
        postfix *= nums[i]
      
      # Default Case: We will return our output array
      return output

    