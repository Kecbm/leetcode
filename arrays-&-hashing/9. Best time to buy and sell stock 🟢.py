from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dict = {}
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                # Um dict para guardar o dia que comprei e vendi (i, j)
                # Guarda também o profit (prices[j] - prices[i])
                dict[(i, j)] = prices[j] - prices[i]
        
        # print(f"Dict: {dict}")

        if not dict:
            return 0
        
        # Pegar o maior profit do dict
        max_profit = max(dict.values())
        # print(f"Max profit: {max_profit}")
        return max_profit if max_profit > 0 else 0
    
solution = Solution()
result = solution.maxProfit([10,1,5,6,7,1]) # profit = 7 - 1 (prices[1] - prices[4])
# print(f"Result: {result}")

"""
Dict: {(0, 1): -9, (0, 2): -5, (0, 3): -4, (0, 4): -3, (0, 5): -9, (1, 2): 4, (1, 3): 5, (1, 4): 6, (1, 5): 0, (2, 3): 1, (2, 4): 2, (2, 5): -4, (3, 4): 1, (3, 5): -5, (4, 5): -6}
Max profit: 6
Result: 6
"""
