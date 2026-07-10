class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Step 1: We need to create an output array, and two pointers: prefix & postfix
        output = [1] * len(nums)
        prefix = 1
        postfix = 1

        #Step 2: We need to first iterate through the array forwards
        for i in range(0, len(nums)):
            #Step 3: We need to make our output[i] value the prefix
            output[i] = prefix

            #Step 4: We need to then update our prefix value and mulitply it by 
            prefix *= nums[i]
        
        #Step 5: We will then traverse backwards to get out postfix value
        for i in range(len(nums)-1,-1,-1):
            output[i] = postfix * output[i]
            postfix *= nums[i]


        #Default Case - We are going to return the output array after we find our prefix/postfix values
        return output
            
        

        
        