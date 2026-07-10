class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       #Step 1: We need to create an output array and 2 pointers: postfix and prefix
       output = [1] * len(nums)
       prefix = 1
       postfix = 1

       #Step 2: We need to now traverse through our array forwards
       for i in range(0,len(nums)):
        #Step 3: We need to put our updated prefix values into our output
        output[i] = prefix
        #Step 4: We need to now update our prefix value with whatever numebr is at the index of our number 
        prefix *= nums[i]
       
       #Step 5: We need to now traverse backwards to make sure that every number at output[i]
       for i in range(len(nums)-1,-1,-1):
          #Step 6: We need to multiply our output[i] by our postfix
          output[i] *= postfix
          #Step 7: Then we need to update our postfix value with whatever our number value is at nums[i]
          postfix *= nums[i]
        
       #Default Case: We need to now show our updated otuput array
       return output

        