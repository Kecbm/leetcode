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


# 🏆 Solution
# Hash Set

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)
        # print(f"🔢 Created set: {num_set}")
        n = len(nums)
        # print(f"📏 Array length: {n}")
        for i in range(n + 1):
            # print(f"🔍 Checking if {i} is in set: {i in num_set}")
            if i not in num_set:
                # print(f"🎯 Missing number found: {i}")
                return i
            
solution2 = Solution2()
result = solution2.missingNumber([0,2])

"""
🔢 Created set: {0, 2}
📏 Array length: 2
🔍 Checking if 0 is in set: True
🔍 Checking if 1 is in set: False
🎯 Missing number found: 1
"""
