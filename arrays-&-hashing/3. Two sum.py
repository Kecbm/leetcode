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
print(f"Result: {result}")

"""
    Found: nums[0] + nums[1] = 3 + 4 = 7
    Result: [0, 1]
"""
