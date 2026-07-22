class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Step 1: We need to create out pointers for our values, so our left and then right pointers and then our max_profit
        left = 0
        right = 1
        max_profit = 0

        #Step 2: We then need to check each time left pointer is then right pointer
        while left < right and right < len(prices):

            #Step 3: We will calcualte our curr_profit
            curr_profit = prices[right] - prices[left]

            #Step 4: We then need to calculate our max_profit from this
            max_profit = max(curr_profit, max_profit)

            #Step 5: We will then update our pointers, if our left pointer greater than right we will increment right, else we will increment left
            if prices[left] > prices[right]:
                left = right # This is our new minimum now
            
            #We will increment right if this is the case
            right += 1
            

        
        # Default Case: We will then return the max profit
        return max_profit
        