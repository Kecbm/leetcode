class Solution:
    def isValid1(self, s: str) -> bool:
        if "[" in s and "]" in s:
            return True
        else:
            return False
    
solution = Solution()
result = solution.isValid1("[]")
# print(f"Result: {result}")
