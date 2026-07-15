class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Step 1: Create a frequency hash map for our key and values
        freq_map = {}

        #Step 2: We need to key/value pairs
        for i,s in enumerate(strs):
            #Step 3: We need to create our char array
            char_array = [0] * 26

            #Step 4: We need to create a 2nd loop for chars
            for c in s:
                #Step 5: We need to now create a counter for each char frequency
                char_array[ord(c) - ord('a')] += 1
                
            #Step 6: We need to now turn our char array into a tuple which is our key
            key = tuple(char_array)

            #Step 7: We need to now check if its in freq_map, if not we will make the key equal to a seperate sublist
            if key in freq_map:
                freq_map[key].append(s)
            else:
                freq_map[key] = [s]
        #Return only the values
        return list(freq_map.values())




