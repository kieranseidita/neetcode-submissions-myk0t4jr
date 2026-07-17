class Solution:
    def isPalindrome(self, s: str) -> bool:
       #Step 1: Create two pointers
       a = 0
       b = len(s) - 1

       #Step 2: We will now iterate through, first conditon will be pointer a, 2nd condiion will be pointer b, and then
       while a < b:
          #Step 3: We will check the condition of a and if its alphanumeric and will move my pointer
          while a < b and not s[a].isalnum():
            a += 1
          #Step 4: We will check the condtion of b and if its alphanumeric and will move my pointer
          while b > a and not s[b].isalnum():
            b -= 1
          #Step 5: We will now check if there are lowercase and will move our pointers
          if s[a].lower() == s[b].lower():
            a += 1
            b -= 1
          else:
            return False
       #Default Case: This will be our default case
       return True