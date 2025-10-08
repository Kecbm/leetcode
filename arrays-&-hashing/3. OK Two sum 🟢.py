from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> bool:
        for i, num in enumerate(nums):
            # Diferença entre o target e o número atual
            diff = target - num
            # print(f"Diff: {diff}")

            if diff in nums[i+1:]:
                # O que falta para chegar no target
                # Buscando com "i+1" porque o diff pode ser igual ao num
                # Exemplo: nums=[5,5] e target=10
                second_num = nums.index(diff, i+1)
                # print(f"Second num: {second_num}")
                return [i, second_num]

solution = Solution()
result = solution.twoSum([3,4,5,6], 7)
# print(f"Result: {result}")

"""
Diff: 4
Second num: 1
Result: [0, 1]
"""
