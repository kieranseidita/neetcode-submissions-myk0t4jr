class Solution:

    def encode(self, strs: List[str]) -> str:
        #Step 1: Create a return string
        encoded_string = ""

        #Step 2: We need to go through all the strings
        for s in strs:
            # Step 3: We need to get the length of our string
            s_count = len(s) 

            #Step 4: We need to 
            s_delim = "#"

            #Step 5: We need to create our encoded string with the length and 
            encoded_string += str(s_count) + s_delim + s
        
        # Default Case: We will return our encoded_string
        return encoded_string
        
        
    def decode(self, s: str) -> List[str]:

        #Step 1: Create a decoded_strs array
        decoded_strs = []

        #Step 2: Create a variable that will keep track of the chars in our string
        i = 0

        #Step 3: We will create a while loop to 
        while i < len(s):
            #Step 4: We will create a 2nd variable to check for our delimeter
            j = s.find("#",i)

            #Step 5: We will then find the length of our word, which will by an integer
            length = int(s[i:j])

            #Step 6: We will then find our word with this
            word = s[j+1:j+1+length]

            #Step 7: We will then add our word to our list of strings
            decoded_strs.append(word)

            #Step 8: We will then update our i to represent our next word
            i = j + 1 + length
        
        #Step 9: We will then return the decoded strings
        return decoded_strs