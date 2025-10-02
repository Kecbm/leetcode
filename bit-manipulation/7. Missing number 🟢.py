from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list_ordered = sorted(nums)
        # print(f"List ordered: {list_ordered}")

        for i in range(len(list_ordered)):
            # Verifica se o primeiro número é zero
            if list_ordered[0] != 0:
                return 0

            # Verifica os próximos números da lista
            if list_ordered[i] != i:
                # print(f"Missing number: {i}")
                return i
            
            # Verifica o último elemento
            if list_ordered[-1] != len(list_ordered):
                # print(f"Last element: {len(list_ordered)}")
                return len(list_ordered)

solution = Solution()
result = solution.missingNumber([3,0,1])
# print(f"Result: {result}")

"""
List ordered: [0, 1, 3]
Missing number: 2
Result: 2
"""
