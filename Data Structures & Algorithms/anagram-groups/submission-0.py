class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Step 1: Creating a hashmap for the result that we will have for our hashmap of sublists
        hashmap_result = defaultdict(list)

        # Step 2: We need to first iterate through the array of string
        for s in strs:

            #Step 3: We need to now create an array containing all 26 characters from a to z
            count = [0] * 26

            #Step 4: We need to now iterate thrugh each character within the string
            for c in s:
                #Step 5: We need to increment the values by 1 so that we count the characters and their exact count in the string
                count[ord(c) - ord('a')] += 1

            #Step 6: Now that we have counted all the character, we will now add our key(or pattern of specific characters and their count to the hashmap) and our value to the list of anagrams for that key pattern
            #Make our array of characters tuple so that they're non-mutable
            hashmap_result[tuple(count)].append(s)

        #Step 7: Now we must return all the values which are list of anagrams in a list
        return list(hashmap_result.values())