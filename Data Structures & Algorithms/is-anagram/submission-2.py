class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Step 1: Check to see if the lengths of both strings are the same or not in order to run our solution
        if len(s) != len(t):
            return False

        #Step 2: Create our 2 Hashmaps for our strings
        hashmap_s, hashmap_t = {}, {}

        #Step 3: Make sure that we can iterate through each string once and increment through it by `1, and get a defautl value of 0
        #Remember that s[i] /t[i] is our key and in our get function, it a function that retrivees both a hashmap key and value
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0)
        
        #Step 4: Now we need to check if our hashmap do or dont contain the exact same count of each character
        for c in hashmap_s:
            if hashmap_s.get(c) != hashmap_t.get(c):
                return False

        #Step 5: This is our default case since we are assuming each time that it is an anagram
        return True
    