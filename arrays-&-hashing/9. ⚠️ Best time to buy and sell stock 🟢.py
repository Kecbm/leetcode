from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0

        if not prices or len(prices) < 2:
            return 0

        for i in range(len(prices)):
            if prices[i] < prices[min]:
                min = i

        print(f"Min: {min}")

        max = min

        for i in range(min, len(prices)):
            if prices[i] > prices[max]:
                max = i
        
        print(f"Max: {max}")

        return prices[max] - prices[min]
    
solution = Solution()
result = solution.maxProfit([10,1,5,6,7,1]) # profit = 7 - 1 (prices[1] - prices[4])
print(f"Result: {result}")