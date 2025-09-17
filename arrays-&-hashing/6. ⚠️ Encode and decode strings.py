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
