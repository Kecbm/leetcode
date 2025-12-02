class Solution:
    def getSum(self, a: int, b: int) -> int:
        return sum((a, b))

solution = Solution()
result = solution.getSum(1, 1)
# print(f"Result: {result}")

"""
Result: 2
"""

# 🏆 Solution
# Brute Force

class Solution2:
    def getSum2(self, a: int, b: int) -> int:
        return a + b

solution2 = Solution2()
result = solution2.getSum2(4, 7)
# print(f"Result: {result}")

"""
Result: 11
"""