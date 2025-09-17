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
# print(f"Result: {result}")
"""
Result: False
"""

class Solution3:
    def validated(self, s: str, expected: str) -> bool:
        for i in range(1, len(expected)):
            if s[i] != expected[i - 1]:
                return False
        
        return True
    
    def isValid3(self, s: str) -> bool:
        if len(s) < 2:
            return False

        if len(s) == 2:
            if s.startswith("("):
                return s.endswith(")")
            if s.startswith("["):
                return s.endswith("]")
            if s.startswith("{"):
                return s.endswith("}")

        if s.startswith("("):
            return self.validated(s, "[{}])")
        
        if s.startswith("["):
            return self.validated(s, "{}]")
        
        if s.startswith("{"):
            return self.validated(s, "}")
        
solution3 = Solution3()
result = solution3.isValid3("[]")
print(f"Result: {result}")
"""
Result: True
"""
