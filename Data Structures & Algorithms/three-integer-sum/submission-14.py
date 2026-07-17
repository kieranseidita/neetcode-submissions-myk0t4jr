class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       #Step 1; We will first sort our array
       nums = sorted(nums) 

       #Step 2: We will create our a variable and keep it at 0
       a = 0

       #Step 3: We will create a output array
       output = []

       #Step 4: We will check for a at a certain range when looking for our 2 pointers b and c, the minus 2 is so that we can have room to add them
       for a in range(0, len(nums)-2):
          #Step 5: We will check if our a ever moves or not
          if a > 0 and nums[a] == nums[a -1]:
             continue
          #Step 6: We will make sure that our left pointer is less than our right pointer and make sure to define our pointers
          b = a + 1
          c = len(nums) - 1
          while b < c:
            #We will have a sum variable so that we dont have to manullay type this if
            our_sum = nums[a] + nums[b] + nums[c]
            #Step 7: If our_sum is greater than 0 we must decrement c, if less than we will increment b
            if our_sum > 0:
                c -= 1
            elif our_sum < 0:
                b +=1
            else:
                #Step 8: We will append the 3Sum sublist in our output array
                output.append([nums[a],nums[b],nums[c]])
                #Continue to move our pointers forward/backward
                b+=1
                c-=1
                #Step 9: We will check the conditions to make sure that our pointers meet certain conditions
                while b < c and nums[b] == nums[b - 1]:
                    b +=1
                while c > b and nums[c] == nums[c + 1]:
                    c -=1
       
       # Default Case - We will return our output array
       return output
     
