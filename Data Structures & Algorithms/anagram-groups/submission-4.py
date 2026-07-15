class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       #Step 1: Create a frequency map
       freq_map = {}
       
       #Step 2: Iterate through the array
       for s in strs:
        #Step 3: Create a char_array to keep track of each character in the alphabet
        char_array = [0] * 26
        
        #Step 4: We now need to go through each character 
        for c in s:
            #Step 5: We need to count each character that we find
            char_array[ord(c) - ord('a')] += 1
          
        #Step 6: Turn our char_array into a tuple for our key
        key = tuple(char_array)

        if key in freq_map:
            freq_map[key].append(s)
        else:
             freq_map[key] = [s]
           
       return list(freq_map.values())


