class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf = 0

        for x in range(len(prices)):
            #took a hint, used to be: for y in range(1,len(prices)):
            for y in range(x + 1, len(prices)):
                if prices[y] - prices[x] > maxProf:
                    maxProf = prices[y] - prices[x]

        return maxProf