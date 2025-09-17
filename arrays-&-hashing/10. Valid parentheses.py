class Solution:
    def isValid1(self, s: str) -> bool:
        if "[" in s and "]" in s:
            return True
        else:
            return False
    
solution = Solution()
result = solution.isValid1("[]")
# print(f"Result: {result}")

"""
Result: True
"""

class Solution2:
    def isValid2(self, s: str) -> bool:
        if s.startswith("("):
            expected = "[{}])"

            for i in range(1, len(expected)):
                if s[i] != expected[i - 1]:
                    return False
            
            return True
        
        if s.startswith("["):
            expected = "{}]"

            for i in range(1, len(expected)):
                if s[i] != expected[i - 1]:
                    return False
            
            return True
        
        if s.startswith("{"):
            expected = "}"

            for i in range(1, len(expected)):
                if s[i] != expected[i - 1]:
                    return False
            
            return True

solution2 = Solution2()
result = solution2.isValid2("([{}])")
# print(f"Result: {result}")
"""
Result: True
"""

solution2 = Solution2()
result = solution2.isValid2("[(])")
print(f"Result: {result}")
"""
Result: False
"""
