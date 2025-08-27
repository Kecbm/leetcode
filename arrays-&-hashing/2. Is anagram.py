# 🥷🏾 FIRST SOLUTION
    # Memory: 52.7 MB
    # Runtime: 2.571 seconds
    # Time complexity: O(n^2)
    # Space complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s = s.lower()
        t = t.lower()

        for letter in s:
            # Quando você faz palavra1.count(letra), o Python:
            # 1. Percorre cada caractere da string palavra1
            # 2. Compara cada caractere com 'letra'
            # 3. Incrementa um contador interno a cada match
            # 4. Retorna o total de ocorrências
            countS = s.count(letter)
            countT = t.count(letter)

            # print(f"Letter '{letter}': countS={countS}, countT={countT}")

            if countS != countT:
                return False

        return True

# Criar instância e testar
solution = Solution()
result = solution.isAnagram("amor", "roma")
print(f"Result: {result}")

"""
    Letter 'a': countS=1, countT=1
    Letter 'm': countS=1, countT=1
    Letter 'o': countS=1, countT=1
    Letter 'r': countS=1, countT=1
    Result: True
"""

# 🥷🏾 SECOND SOLUTION
    # Memory: 52 MB
    # Runtime: 0.9 seconds
    # Complexity: O(n)
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Counter cria um dicionário com a contagem de cada caractere
        # counter_s = Counter(s)
        # counter_t = Counter(t)

        # print(f"Counter(s): {counter_s}")
        # print(f"Counter(t): {counter_t}")

        # return counter_s == counter_t

        return Counter(s) == Counter(t)

solution = Solution()
result = solution.isAnagram("ator", "rota")
print(f"Result: {result}")

"""
    Counter(s): Counter({'a': 1, 't': 1, 'o': 1, 'r': 1})
    Counter(t): Counter({'r': 1, 'o': 1, 't': 1, 'a': 1})
    Result: True
"""

# 🥷🏾 THIRD SOLUTION
    # Memory: 52.4 MB
    # Runtime: 0.816 seconds
    # Complexity: O(n)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # print(f"Sorted s: {sorted_s}")
        # print(f"Sorted t: {sorted_t}")

        # return sorted_s == sorted_t
        
        return sorted(s) == sorted(t)

solution = Solution()
result = solution.isAnagram("cinema", "iceman")
print(f"Result: {result}")

"""
    Sorted s: ['a', 'c', 'e', 'i', 'm', 'n']
    Sorted t: ['a', 'c', 'e', 'i', 'm', 'n']
    Result: True
"""
