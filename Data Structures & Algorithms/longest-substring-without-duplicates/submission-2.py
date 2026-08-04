class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Step 1: Lets create our left pointer, our max_length of our substring, and the set that will store our characters, our right pointer will be defined by our range
        max_length = 0
        my_set = set()
        left = 0
        for right in range(len(s)):
            #Step 2: We will check to see if our
            while s[right] in my_set:
                #Step 3: We will now remove the character and left, if we are shrinking the window
                my_set.remove(s[left])
                left += 1
            
            #Step 4: We will then add if s[right] is not in the set
            my_set.add(s[right])
            
            #Step 4: We need to keep track of all the length
            max_length = max(max_length, right - left + 1)
        
        # Default Case: We will return the max length of our longest substring
        return max_length

