class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #Step 1: Create a hashmap for our values to look through their value and their index
        hash_map = {}

        #Step 2: Now we must iterate through both the index and the current value at that index
        for index, current_val in enumerate(nums):

            #Step 3: Create the difference variable containing target and current value at a certain index
            difference = target - current_val

            #Step 4: If we happen to have our difference contained in our hashmap, we will return the value at the hashmap and then the current index
            if difference in hash_map:
                return [hash_map[difference], index]

            #Step 5: If we don't find difference contained in hashmap, we then need to then to move on to the next current value which is at index in nums, which we will add to our hashmap
            hash_map[current_val] = index
        
        #This is the default use case for when we dont have any integers to look through
        return []