class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Step 1: We will initiatlize our two pointers
        a = 0
        b = len(s) - 1

        #Step 2: We will now create our while loop for this problem to check
        while a < b:
            #Step 3: Need to check how a is before increment
            while a < b and  not s[a].isalnum():
                a += 1

            #Step 4: Need to check how b is before decrement
            while b > a  and  not s[b].isalnum():
                b -= 1

            #Step 5: We need to check is there are lower so we can move our pointers
            if s[a].lower() == s[b].lower():
                a += 1
                b -= 1
            else:
                return False
            
        #Default Case:
        return True