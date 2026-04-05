class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Step 1: We need to check to see if the length of the 2 strings are equal so that we return false
        if len(s) != len(t):
            return False

        #Step 2: We need to now create a hashmap for both string to keep track of their 
        # Key which is their character adn their values which is the frequency at whihc that character appears
        hashmap_s, hashmap_t = {}, {}

        #Step 3: Now we need to check & count each character at each index with the same length as our first string
        #We are checking each key first
        for i in range(len(s)):
            hashmap_s[s[i]] = 1 + hashmap_s.get(s[i], 0)
            hashmap_t[t[i]] = 1 + hashmap_t.get(t[i], 0)

        #Now we need to check if both are aligned just going through the first hashmap
        for c in hashmap_s:
            if hashmap_s.get(c,0) != hashmap_t.get(c,0):
                return False


        #Our Default case is that we assume that they are both anagrams
        return True