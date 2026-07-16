class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       #Step 1: Create a hash_set that will contain all of our numbers 
       hash_set = set()
       max_consec = 0

       #Step 2: We will iterate through our array and the numbers that are contained and add it to our hash_set
       for num in nums: 
        hash_set.add(num)
        #Step 3: We need to now check all the number that are contained within our hash_set
       for n in hash_set:
            if n - 1 not in hash_set:
                start_consec = 1
                while n + start_consec in hash_set:
                    start_consec += 1 
                #Step 4: We will check each time whether we need to update our max consecutive sequence
                max_consec = max(max_consec, start_consec)

       #Default Case:
       return max_consec