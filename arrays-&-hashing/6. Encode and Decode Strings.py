# 🥷🏾 SOLUTION
from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Transformar uma lista de strings em uma única string
        separator = "#"

        # Juntar todas as strings com o separador
        encoded = ""

        for i in range(len(strs)):
            encoded += strs[i]

            # Não adiciona o separador depois da última string
            if i < len(strs) - 1:
                encoded += separator
            
            # print(f"Encoded: {encoded}")
        
        return encoded
    
solution = Solution()
result = solution.encode(["Meg", "Kali", "Laila", "Luna", "Mel", "Jaia", "Juno"])
# print(f"Result: {result}")

"""
    Encoded: Meg#
    Encoded: Meg#Kali#
    Encoded: Meg#Kali#Laila#
    Encoded: Meg#Kali#Laila#Luna#
    Encoded: Meg#Kali#Laila#Luna#Mel#
    Encoded: Meg#Kali#Laila#Luna#Mel#Jaia#
    Encoded: Meg#Kali#Laila#Luna#Mel#Jaia#Juno
    Result: Meg#Kali#Laila#Luna#Mel#Jaia#Juno
"""

class Solution2:
    def decode(self, s: str) -> List[str]:
        # Transformar uma string em uma lista de strings
        separator = "#"

        # Dividir a string pelo separador
        decode = s.split(separator)

        return decode

solution2 = Solution2()
result = solution2.decode("Guitar Hero III#CSGO#Gran Turismo 6#Fifa 19")
# print(f"Result: {result}")

"""
    Result: ['Guitar Hero III', 'CSGO', 'Gran Turismo 6', 'Fifa 19']
"""

# Co authored with Augment
class Solution3:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            # Formato: comprimento + "#" + string
            encoded += str(len(s)) + "#" + s
            # print(f"Encoded: {encoded}")
        return encoded
    
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            # Encontrar o delimitador "#"
            j = s.find("#", i)
            print(f"Delimiter: {j}")
            # Extrair o comprimento
            length = int(s[i:j])
            print(f"Length: {length}")
            # Extrair a string usando o comprimento
            result.append(s[j +1:j + 1 + length])
            print(f"Result: {result}")
            # Mover para a próxima string
            i = j + 1 + length
            print(f"Next: {i}")
        
        return result


solution3 = Solution3()
result = solution3.encode(["Django", "5", "by", "Example"])
# print(f"Result: {result}")

"""
    Encoded: 6#Django
    Encoded: 6#Django1#5
    Encoded: 6#Django1#52#by
    Encoded: 6#Django1#52#by7#Example
    Result: 6#Django1#52#by7#Example
"""

solution3 = Solution3()
result = solution3.decode("6#Django1#52#by7#Example")
print(f"Result: {result}")

"""
    Delimiter: 1
    Length: 6
    Result: ['Django']
    Next: 8
    Delimiter: 9
    Length: 1
    Result: ['Django', '5']
    Next: 11
    Delimiter: 12
    Length: 2
    Result: ['Django', '5', 'by']
    Next: 15
    Delimiter: 16
    Length: 7
    Result: ['Django', '5', 'by', 'Example']
    Next: 24
    Result: ['Django', '5', 'by', 'Example']
"""
