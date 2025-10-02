class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # print(f"S1: {s1}")
        # print(f"S2: {''.join(sorted(s2))}")
        return s1 in ''.join(sorted(s2))
    
solution = Solution()
result = solution.checkInclusion("abc", "lecabee")
# print(f"Result: {result}")
"""
Result: True
"""

class Solution2:
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        count_s2 = {}
        count_s1 = {}

        for letter in s2:
            # Guarda a ocorrência de cada letra da string 2
            count_s2[letter] = count_s2.get(letter, 0) + 1
            # print(f"Count s2: {count_s2}")

        for letter in s1:
            # Guarda a ocorrência de cada letra da string 2
            count_s1[letter] = count_s1.get(letter, 0) + 1
            # print(f"Count s1: {count_s1}")

        # Filtra s2 pelas letras de s1
        filtered_s2 = {k: v for k, v in count_s2.items() if k in count_s1}
        # print(f"Filtered s2: {filtered_s2}")
        
        return count_s1 == filtered_s2
    
solution2 = Solution2()
result = solution2.checkInclusion2("abc", "lecaabee")
# print(f"Result: {result}")
"""
Count s2: {'l': 1}
Count s2: {'l': 1, 'e': 1}
Count s2: {'l': 1, 'e': 1, 'c': 1}
Count s2: {'l': 1, 'e': 1, 'c': 1, 'a': 1}
Count s2: {'l': 1, 'e': 1, 'c': 1, 'a': 2}
Count s2: {'l': 1, 'e': 1, 'c': 1, 'a': 2, 'b': 1}
Count s2: {'l': 1, 'e': 2, 'c': 1, 'a': 2, 'b': 1}
Count s2: {'l': 1, 'e': 3, 'c': 1, 'a': 2, 'b': 1}
Count s1: {'a': 1}
Count s1: {'a': 1, 'b': 1}
Count s1: {'a': 1, 'b': 1, 'c': 1}
Filtered s2: {'c': 1, 'a': 2, 'b': 1}
Result: False
"""

# 🏆 Solution

class Solution3:
    def checkInclusion3(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        # print(f"S1 ordenado: {s1}")
        # print(f"S2 original: {s2}")
        # print("-" * 40)

        for i in range(len(s2)):
            # print(f"\n🔍 Iniciando na posição {i} ('{s2[i]}')")
            
            for j in range(i, len(s2)):
                subStr = s2[i : j + 1]
                subStr_sorted = sorted(subStr)
                
                # print(f"  Substring: '{subStr}' → ordenada: {subStr_sorted}")
                
                if subStr_sorted == s1:
                    # print(f"  ✅ ENCONTROU! '{subStr}' é permutação de {''.join(s1)}")
                    return True
                else:
                    # print(f"  ❌ Não é igual a {s1}")
        
                    # print(f"\n🛑 Nenhuma permutação encontrada")
                    return False
    
solution3 = Solution3()
result = solution3.checkInclusion3("ab", "eidboaoo")
# print(f"Result: {result}")
"""
S1 ordenado: ['a', 'b']
S2 original: eidboaoo
----------------------------------------

🔍 Iniciando na posição 0 ('e')
  Substring: 'e' → ordenada: ['e']
  ❌ Não é igual a ['a', 'b']
  Substring: 'ei' → ordenada: ['e', 'i']
  ❌ Não é igual a ['a', 'b']
  Substring: 'eid' → ordenada: ['d', 'e', 'i']
  ❌ Não é igual a ['a', 'b']
  Substring: 'eidb' → ordenada: ['b', 'd', 'e', 'i']
  ❌ Não é igual a ['a', 'b']
  Substring: 'eidbo' → ordenada: ['b', 'd', 'e', 'i', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'eidboa' → ordenada: ['a', 'b', 'd', 'e', 'i', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'eidboao' → ordenada: ['a', 'b', 'd', 'e', 'i', 'o', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'eidboaoo' → ordenada: ['a', 'b', 'd', 'e', 'i', 'o', 'o', 'o']
  ❌ Não é igual a ['a', 'b']

🔍 Iniciando na posição 1 ('i')
  Substring: 'i' → ordenada: ['i']
  ❌ Não é igual a ['a', 'b']
  Substring: 'id' → ordenada: ['d', 'i']
  ❌ Não é igual a ['a', 'b']
  Substring: 'idb' → ordenada: ['b', 'd', 'i']
  ❌ Não é igual a ['a', 'b']
  Substring: 'idbo' → ordenada: ['b', 'd', 'i', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'idboa' → ordenada: ['a', 'b', 'd', 'i', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'idboao' → ordenada: ['a', 'b', 'd', 'i', 'o', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'idboaoo' → ordenada: ['a', 'b', 'd', 'i', 'o', 'o', 'o']
  ❌ Não é igual a ['a', 'b']

🔍 Iniciando na posição 2 ('d')
  Substring: 'd' → ordenada: ['d']
  ❌ Não é igual a ['a', 'b']
  Substring: 'db' → ordenada: ['b', 'd']
  ❌ Não é igual a ['a', 'b']
  Substring: 'dbo' → ordenada: ['b', 'd', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'dboa' → ordenada: ['a', 'b', 'd', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'dboao' → ordenada: ['a', 'b', 'd', 'o', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'dboaoo' → ordenada: ['a', 'b', 'd', 'o', 'o', 'o']
  ❌ Não é igual a ['a', 'b']

🔍 Iniciando na posição 3 ('b')
  Substring: 'b' → ordenada: ['b']
  ❌ Não é igual a ['a', 'b']
  Substring: 'bo' → ordenada: ['b', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'boa' → ordenada: ['a', 'b', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'boao' → ordenada: ['a', 'b', 'o', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'boaoo' → ordenada: ['a', 'b', 'o', 'o', 'o']
  ❌ Não é igual a ['a', 'b']

🔍 Iniciando na posição 4 ('o')
  Substring: 'o' → ordenada: ['o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'oa' → ordenada: ['a', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'oao' → ordenada: ['a', 'o', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'oaoo' → ordenada: ['a', 'o', 'o', 'o']
  ❌ Não é igual a ['a', 'b']

🔍 Iniciando na posição 5 ('a')
  Substring: 'a' → ordenada: ['a']
  ❌ Não é igual a ['a', 'b']
  Substring: 'ao' → ordenada: ['a', 'o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'aoo' → ordenada: ['a', 'o', 'o']
  ❌ Não é igual a ['a', 'b']

🔍 Iniciando na posição 6 ('o')
  Substring: 'o' → ordenada: ['o']
  ❌ Não é igual a ['a', 'b']
  Substring: 'oo' → ordenada: ['o', 'o']
  ❌ Não é igual a ['a', 'b']

🔍 Iniciando na posição 7 ('o')
  Substring: 'o' → ordenada: ['o']
  ❌ Não é igual a ['a', 'b']

🛑 Nenhuma permutação encontrada
Result: False
"""
