class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Step 1: Create a hashmap
        hashmap = {}

        #Step 2: We need to iterate through both the index and the current value in our number
        for index, current_val in enumerate(nums):
            
            #Step 3: Create the difference value that we will iterate through when looking through our hashmap
            difference = target - current_val

            #Step 4: Check to see if difference is contained within our hashmap
            if difference in hashmap:

                #Step 5: This is when we
                return[hashmap[difference], index]
            #Step 6: This is then we must assign now the current_val to the index that is now at the location of index

            hashmap[current_val] = index

        
        #This is our default value
        return []