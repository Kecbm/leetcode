from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_i = 0
        result = 0
        for i in range(len(height)):

            max_i = max(max_i, height[i])
            print(f"max_i: {max_i}")

            for j in range(1, len(height)):
                if height[i] < height[j]:
                    continue

                if height[i] >= height[j]:
                    if (height[i] == height[j]) == 0:
                        return result
                    
                    result += (max_i - height[j])
                    print(f"result: {result}")

solution = Solution()
result = solution.trap([0,2,0,3,1,0,1,3,2,1])
print(f"Result: {result}")

"""

"""
