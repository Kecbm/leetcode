from typing import List

# 🥷🏾 FIRST SOLUTION
    # Memory: 52.1 MB
    # Runtime: 0.892 seconds

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Percorre os números da lista
        for i in range(len(nums)):
            # Para cada número, verifica todos os números seguintes
            for j in range(i + 1, len(nums)):
                # Se a soma dos dois números é igual ao target
                if nums[i] + nums[j] == target:
                    # print(f"Found: nums[{i}] + nums[{j}] = {nums[i]} + {nums[j]} = {target}")
                    return [i, j]  # Retorna os índices

solution = Solution()
result = solution.twoSum([3, 4, 5, 6], 7)
# print(f"Result: {result}")

"""
    Found: nums[0] + nums[1] = 3 + 4 = 7
    Result: [0, 1]
"""

# 🥷🏾 SECOND SOLUTION
    # Memory: 52.5 MB
    # Runtime: 0.884 seconds

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            needed = target - nums[i]
            # print(f"nums[{i}] = {nums[i]}, need {needed} to reach {target}")

            for j in range(i + 1, len(nums)):
                if nums[j] == needed:
                    # print(f"Found needed number {needed} at index {j}")
                    return [i, j]

solution = Solution()
result = solution.twoSum([1, 3, 7, 9], 10)
# print(f"Result: {result}")

"""
    nums[0] = 1, need 9 to reach 10
    Found needed number 9 at index 3
    Result: [0, 3]
"""
