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
        # Validações da sequência de caracteres padrão
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
    # Refatoração da lógica de validação
    def validated(self, s: str, expected: str) -> bool:
        for i in range(1, len(expected)):
            if s[i] != expected[i - 1]:
                return False
        
        return True
    
    def isValid3(self, s: str) -> bool:
        if len(s) < 2:
            return False

        # Validações da sequência de 2 caracteres
        if len(s) == 2:
            if s.startswith("("):
                return self.validated(s, ")")
            if s.startswith("["):
                return self.validated(s, "]")
            if s.startswith("{"):
                return self.validated(s, "}")

        if s.startswith("("):
            return self.validated(s, "[{}])")
        
        if s.startswith("["):
            return self.validated(s, "{}]")
        
        if s.startswith("{"):
            return self.validated(s, "}")
        
        return False
        
solution3 = Solution3()
result = solution3.isValid3("[]")
# print(f"Result: {result}")
"""
Result: True
"""

class Solution4:
    def validated(self, s: str, expected: str) -> bool:
        for i in range(1, len(expected)):
            if s[i] != expected[i - 1]:
                result = False
                return result
        
        result = True
        return result
    
    def isValid4(self, s: str) -> bool:
        if len(s) < 2:
            result = False

        if len(s) == 2:
            if s.startswith("("):
                result = self.validated(s, ")")
            if s.startswith("["):
                result = self.validated(s, "]")
            if s.startswith("{"):
                result = self.validated(s, "}")

        if s.startswith("("):
            result = self.validated(s, "[{}])")
        
        if s.startswith("["):
            result = self.validated(s, "{}]")

        # Validações do novo tipo de sequência de caracteres
        if s.startswith("("):
            result = self.validated(s, ")[]{}")
        
        if s.startswith("["):
            result = self.validated(s, "]{}")

        return result

solution4 = Solution4()
result = solution4.isValid4("()[]{}")
print(f"Result: {result}")
"""
Result: True
"""

# Example for solution: https://medium.com/codex/leetcode-20-valid-parentheses-python-programming-solution-10aed7025b92
