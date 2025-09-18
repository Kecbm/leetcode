from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            dict[num] = dict.get(num, 0) + 1

        # print(f"Dict: {dict}")

        result = sorted(dict.items(), key=lambda x: x[1], reverse=True)

       # print(f"Dict sorted: {result}")

        return [num for num, freq in result[:k]]

solution = Solution()
result = solution.topKFrequent([1,2,2,3,3,3], 2)
# print(f"Result: {result}")
"""
Result: [1, 2]
"""
