class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       #Step 1: Create a hashmap so that I can store all of my results in a hashmap
       hashmap_result = defaultdict(list)

       #Step 2: Create a 1st for loop iterating through the strings within our array
       for s in strs:
        #Step 3: Create a count array that will contained all characters from a to z
        count = [0] * 26
        #Step 4: Create a 2nd for loop to iterate through each character within each string
        for c in s:
            #Step 5: We need to add 1 of a certain character by finding the character byt taking c and subtracting by the ASCII chaarcter a
            count[ord(c) - ord("a")] += 1
        
        #Step 6: Then we need to take each character and its count and add the string that has that pattern count of characters into our hashmap
        #Make our count array a tuple so that the characters that it creates
        hashmap_result[tuple(count)].append(s)
       
       return list(hashmap_result.values())