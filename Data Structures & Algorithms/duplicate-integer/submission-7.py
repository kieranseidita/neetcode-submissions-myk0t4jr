class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Step 1: Create a hashset for this problem
        hash_set = set()

        #Step 2: We are going to iterate through our list to check for duplicates
        for num in nums:
            #Step 3: We are checkign to see if num that we are checking appears twice
            if num in hash_set:
                #Step 4: We will return true if num becomes a duplciate in the hashset
                return True
            #Step 5:We will add the number to our set if its already not there
            hash_set.add(num)
        
        #Step 6: Default Edge Case - We will return False if we don't find any duplicates
        return False

            
        