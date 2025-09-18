from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            index = nums.index(target)
            return index
        
        return -1

solution = Solution()
result = solution.search([-1,0,2,4,6,8], 4)
print(f"Result: {result}")

"""
Result: 3
"""
