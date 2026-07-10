class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Step 1: We need to create a hash_set
        hash_set = []

        #Step 2: We need to iterate throughout our array 
        for num in nums:
            #Step 3: We need to check to see if our number appears more than once in
            if num in hash_set:
                #Step 4: We will retur
                return True
            
            #Step 5: We will then add it to our hash_set so that we can check if it will contain duplicates
            hash_set.append(num)
        
        #Step 6: We will return false if the value doesn't appear more than once
        return False
            
        