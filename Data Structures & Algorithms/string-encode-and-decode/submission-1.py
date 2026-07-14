class Solution:

    def encode(self, strs: List[str]) -> str:
        #Step 1: We will create an output string
        encoded_string = ""

        #Step 2: We will iterate through each string in our list
        for s in strs:
            #Step 3: We need to find the length
            s_count = len(s)

            #Step 4: We then need to place a delimeter for us to tell if its a word or not
            s_delim = "#"

            #Step 5: We will now use string concatenation in order to add our s_count, s_delim and the content of our string itself
            encoded_string += str(s_count) + s_delim + s

        #As our default case, we will return our encoded_string
        return encoded_string
        
    def decode(self, s: str) -> List[str]:
        #Step 1: We will create our string that we will get
        decoded_strs = []
        i = 0

        #Step 2: We will then check through each character in our encoded string
        while i < len(s):
            #Step 3: Create a variable to see if we find our delimeter which determines if we have a word or not
            j = s.find("#",i)

            #Step 4: We will now find our length
            length = int(s[i:j])

            #Step 5: We will create our word that will append into our list
            word = s[j+1:j+1+length]

            #Step 6: We will then add our word to our list
            decoded_strs.append(word)

            #Step 7: We then need to update our i
            i = j + 1 + length
        #We will now return our decoded list of strings
        return decoded_strs
        