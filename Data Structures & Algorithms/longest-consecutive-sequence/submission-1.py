class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      #Step 1: We need to create 2 variables: a  hashset and then a max_consecutive variable
      hash_set = set()
      max_consec = 0

      #Step 2: We need to now add all of our values to our hash_set
      for num in nums:
        hash_set.add(num)
      
      #Step 3: We now need a 2nd pass to check if its left neighbor is in the hash_set
      for n in hash_set:
        #Step 4: If n -1 isnt in hash_set we assume that we are starting a new sequence
        if n - 1 not in hash_set:
            start_consec = 1
            while n + start_consec in hash_set:
                start_consec += 1
            max_consec = max(max_consec,start_consec)
      
      return max_consec