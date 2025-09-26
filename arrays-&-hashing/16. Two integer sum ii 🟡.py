from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, num in enumerate(numbers):
            diff = target - num
            # print(f"Diff: {diff}")

            if diff in numbers[i+1:]:
                second_num = numbers.index(diff, i+1)
                # print(f"Second num: {second_num}")

                return [i + 1, second_num + 1]

solution = Solution()
result = solution.twoSum([1,2,3,4], 3)
# print(f"Result: {result}")

"""
Diff: 2
Second num: 1
Result: [1, 2]
"""
