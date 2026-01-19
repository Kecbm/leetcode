from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        for i in range(len(nums)):
            # range(start, stop, step)
            # start: onde começa (por default é 0)
            # stop: onde para (não inclui esse número)
            # step: o passo/incremento (por default é 1)
            for j in range(1, len(nums)):
                for k in range(2, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        return [nums[i], nums[j], nums[k]]

solution = Solution()
result = solution.threeSum([-1,0,1,2,-1,-4])
# print(f"Result: {result}")

"""
Result: [-1, 0, 1]
"""