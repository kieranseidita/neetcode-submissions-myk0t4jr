class Solution:
    def isValid(self, s: str) -> bool:
        #Step 1: We need to create a stack and then a hashmap of all of our 
        my_stack = []
        parentheses = {'}':'{', ']':'[', ')':'('}

        #Step 2: We need to make sure that we are now iterating through the characters and check if its in parentheses
        for c in s:
            if c in parentheses:
                if my_stack and my_stack[-1] == parentheses[c]:
                    my_stack.pop()
                else:
                    return False
            else:
                my_stack.append(c)
            
        return True if not my_stack else False