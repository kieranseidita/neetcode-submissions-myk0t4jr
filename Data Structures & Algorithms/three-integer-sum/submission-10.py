class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Step 1: We need to now sort out array in order for this solution to work
        nums = sorted(nums)

        #Step 2: We need to create out left(b) and right(c) pointers and our variable which will be our starting point
        a = 0

        #We also need to create a results array
        output = []

        for a in range(0,len(nums)-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            b = a + 1
            c = len(nums) - 1
            while b < c:
                #Step 3: We need to now check the conditions if our conditons are equal to 0, greater than or less than
                our_sum = nums[a] + nums[b] + nums[c]
                if our_sum > 0:
                    #Step 4: We will Shift our right pointer
                    c -= 1
                elif our_sum < 0:
                    #Step 5: We will shift our right pointer
                    b += 1
                else:
                    #Step 6: We need to now return this values by appending it to our list
                    output.append([nums[a], nums[b], nums[c]])
                    b+=1
                    c-=1
                    #Step 7: We need to add while loop to keep iterating for the right contions
                    while b < c and nums[b] == nums[b-1]:
                        b+=1
                    while c > b and nums[c] == nums[c+1]:
                        c-=1
        
        #Default Case: We will return an empty list we dont get anything
        return output
