# 🥷🏾 FIRST SOLUTION
    # Memory:  52.1 MB
    # Runtime: 0.955 seconds

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Criar set remove duplicatas
        unique_nums = set(nums)
        print(f"Unique nums: {unique_nums}")

        # Se tamanhos diferentes, havia duplicatas
        if len(nums) != len(unique_nums):
            return True
        else:
            return False

solution = Solution()
result = solution.containsDuplicate([1, 2, 3, 3])
print(f"Result: {result}")

"""
    Unique nums: {1, 2, 3}
    Result: True
"""