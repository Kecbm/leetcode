# 🥷🏾 FIRST SOLUTION
    # Memory:  52.1 MB
    # Runtime: 0.955 seconds

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # O set remove números duplicados
        unique_nums = set(nums)
        # print(f"Unique nums: {unique_nums}")

        # Se os arrays forem de tamanhos diferentes, há números duplicados
        if len(nums) != len(unique_nums):
            return True
        else:
            return False

solution = Solution()
result = solution.containsDuplicate([1, 2, 3, 3])
# print(f"Result: {result}")

"""
    Unique nums: {1, 2, 3}
    Result: True
"""

# 🥷🏾 SECOND SOLUTION
    # Memory:  52.3 MB
    # Runtime: 0.861 seconds

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # print(f"Unique nums: {set(nums)}")
        return len(nums) != len(set(nums))
    
solution = Solution()
result = solution.containsDuplicate([4, 4, 5, 6])
# print(f"Result: {result}")

"""
    Unique nums: {4, 5, 6}
    Result: True
"""

# 🥷🏾 THIRD SOLUTION
    # Memory:  52.7 MB
    # Runtime: 0.88 seconds

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            # Para cada número, conta quantas vezes aparece
            # Se algum aparece mais de 1 vez, retorna True
            if nums.count(num) > 1:
                # print(f"Count of {num}: {nums.count(num)}")
                return True
        return False
    
solution = Solution()
result = solution.containsDuplicate([7, 8, 8, 9])
# print(f"Result: {result}")

"""
    Count of 8: 2
    Result: True
"""