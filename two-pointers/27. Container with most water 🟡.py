from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return heights[0] * heights[1]
    
solution = Solution()
result = solution.maxArea([2, 2, 2])
# print(f"Result: {result}")

"""
Result: 4
"""
