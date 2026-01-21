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

class Solution2:
    def maxArea2(self, heights: List[int]) -> int:
        # Two Pointers
        # i is ths left
        right = len(heights) - 1

        for i in range(len(heights)):
            if (heights[i] < heights[right]):
                i += 1
                continue
            
            if (heights[i] <= heights[right]):
                return heights[i] * heights[right]

    
solution2 = Solution2()
result2 = solution2.maxArea2([1,7,2,5,4,7,3,6])
# print(f"Result: {result2}")

"""
Result: 36
"""
