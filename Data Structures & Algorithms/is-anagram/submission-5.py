class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Step 1: We need to check to see if the lengths are the same or not
        if len(s) != len(t):
            return False


        #Step 2:Create 2 different hashmaps in order to compare the character count of the letters
        hashmap_s, hashmap_t = {}, {}

        #Step 3: Now we must iterate through the range of string s to make sure that we are able to count through each of the characters
        for i in range(len(s)):
            #Step 4: We must look through each key and make sure to get the key and value of the characters of the string by incrementing by 1 every time we see a character in the list
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0)

        #Step 5: We then need to go through only one hashmap in order to figure out if the other hashmap of the othe rsrign contains the exact letter or not
        #We need to use the get method when retreving key and value pairs
        for c in hashmap_s:
            if hashmap_s.get(c, 0) != hashmap_t.get(c, 0):
                return False

        #Default Case: We will always assume that these 2 strings are valid anagrams
        return True