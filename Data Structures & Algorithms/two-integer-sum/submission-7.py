class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Step 1: Create a hashamp for out solution
        freq_map = {}

        #Step 2: We will iterate through our array to figure out the difference value
        #enumerate creates key value pairs
        for i, num in enumerate(nums):
            #Step 3: We are going to create a difference variable based on the target
            diff = target - num

            #Step 4: We are going to check to see if our difference is in our frequency map
            if diff in freq_map:
                #Step 5: We will return an array of the values
                return [freq_map[diff], i]
            
            #Step 6: We are going to go to the next number based on the index
            freq_map[num] = i
        