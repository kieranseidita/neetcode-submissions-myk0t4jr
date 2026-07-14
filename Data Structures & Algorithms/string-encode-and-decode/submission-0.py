class Solution:

    def encode(self, strs: List[str]) -> str:
        #Step 1: We need to have an output string which by default will be empty
        encoded_string = ""

        #Step 2: We now now to go through each string that is in our list
        for s in strs:
            #Step 3: We need to now get the count of the string
            s_count = len(s)

            #Step 4: We need to create a delimeter next to the number count
            s_delim = "#"

            #Step 5: We need to now add to our including the string that we are working with
            encoded_string += str(s_count) + s_delim + s

        #Step 6: We will then return the encoded string
        return encoded_string


        
    def decode(self, s: str) -> List[str]:
        #Step 1: We will now create a list that we will return
        decoded_strs = []
        i = 0

        #Step 2: We will now iterate through every character that is contained within our string
        while i < len(s):
            #Step 3: We will now first look for the delimeter 
            j = s.find("#",i)

            #Step 4: We then need to find the length
            length = int(s[i:j])

            #Step 5: We need the word itself, which will be after our delimiter
            word = s[j+1:j+1+length]

            #Step 4: We will then look thrugh the delimeter and just count the word that we want to add to our list
            decoded_strs.append(word)

            #Step 5: We will then update our i which will be each encoded string
            i = j + 1 + length

        #Step 6: We will return our decoded strings
        return decoded_strs