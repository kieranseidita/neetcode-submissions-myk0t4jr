class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #Step 1: Create a hashset, since we are mapping any value we are just adding values to hashset
        hash_set = set()

        #Step 2: We must iterate through our list/array
        for i in nums:
            #Step 3: We must to check if i is contained in nums to see if there is a duplicate, whichw e will return true
            if i in hash_set:
                return True
            
            #Step 4: If there contains no duplicate, we will add our number to the hash set
            hash_set.add(i)
        #Step 5: We have our default return statement, which is false
        return False

    
        