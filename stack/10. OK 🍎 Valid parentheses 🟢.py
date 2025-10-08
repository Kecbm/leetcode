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
result = solution3.isValid3("{}")
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
# print(f"Result: {result}")
"""
Result: True
"""

# 🏆 Solution: Brute Force

class Solution5:
    def isValid5(self, s: str) -> bool:
        # Enquanto houver pares válidos de parênteses na string
        # Continue removendo eles até que não sobre nenhum
        while '()' in s or '{}' in s or '[]' in s:
            # Remove todos os pares válidos encontrados
            # Isso funciona porque pares válidos sempre podem ser removidos
            # sem afetar a validade dos outros pares

            print(f"String: {s}")

            s = s.replace('()', '') # Remove parênteses
            s = s.replace('{}', '') # Remove chaves
            s = s.replace('[]', '') # Remove colchetes

        # Se a string ficou vazia, significa que todos os parênteses
        # estavam corretamente balanceados e puderam ser removidos
        # Se sobrou algo, significa que havia parênteses desbalanceados
        print(f"Final string: {s}")
        return s == ''

solution5 = Solution5()
# result1 = solution5.isValid5("[]")
# print(f"Result: {result1}")
"""
String: []
Final string: 
Result: True
"""

# result2 = solution5.isValid5("([{}])")
# print(f"Result: {result2}")
"""
String: ([{}])
String: ()
Final string: 
Result: True
"""

# result3 = solution5.isValid5("[(])")
# print(f"Result: {result3}")
"""
Final string: [(])
Result: False
"""

result4 = solution5.isValid5("()[]{}")
print(f"Result: {result4}")
"""
String: ()[]{}
Final string: 
Result: True
"""

# 🍎 @Faamk - Stack/Pilha

class Solution6:
    symbol_map = {  '(':')',
                    '[':']',
                    '{':'}'}
    def isValid6(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in self.symbol_map:
                stack.append(self.symbol_map[c]) 
            else:
                if not stack or stack[-1] != c:
                    return False
                stack.pop()

        return not stack
